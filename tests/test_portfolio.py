"""Homepage integration checks; run with python -m unittest discover -s tests."""
from html.parser import HTMLParser
from unittest import TestCase
from urllib.parse import urlsplit

from werkzeug.test import Client
from werkzeug.wrappers import Response

from app import create_app


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class PortfolioTests(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        # Werkzeug's WSGI client also works with the existing Flask 2.3 pin
        # and newer Werkzeug versions that lack __version__.
        self.client = Client(self.app, Response)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.page = PageParser()
        self.page.feed(response.get_data(as_text=True))

    def test_heading_structure_and_anchor_targets(self):
        elements = self.page.elements
        self.assertEqual(sum(tag == 'h1' for tag, _ in elements), 1)
        ids = [attrs['id'] for _, attrs in elements if 'id' in attrs]
        self.assertEqual(len(ids), len(set(ids)), 'Duplicate HTML IDs')
        for tag, attrs in elements:
            if tag == 'a' and attrs.get('href', '').startswith('#'):
                self.assertIn(attrs['href'][1:], ids)

    def test_static_assets_are_served_and_images_have_alt_text(self):
        for tag, attrs in self.page.elements:
            if tag == 'img':
                self.assertTrue(attrs.get('alt'))
            path = attrs.get('src') or attrs.get('href', '')
            if path.startswith('/static/'):
                with self.subTest(path=path):
                    with self.client.get(path) as response:
                        self.assertEqual(response.status_code, 200)

    def test_project_filters_cover_every_card_and_no_script_fallback(self):
        filters = {attrs['data-filter'] for _, attrs in self.page.elements
                   if 'data-filter' in attrs}
        cards = [attrs for tag, attrs in self.page.elements if tag == 'article']
        self.assertEqual(len(cards), 6)
        for card in cards:
            self.assertIn(card['data-category'], filters)
            self.assertNotIn('hidden', card, 'Projects must render without JS')
        toolbars = [attrs for _, attrs in self.page.elements
                    if attrs.get('class') == 'project-toolbar']
        self.assertIn('hidden', toolbars[0])

    def test_external_links_and_contact_destinations(self):
        links = [attrs for tag, attrs in self.page.elements if tag == 'a']
        self.assertTrue(any(attrs.get('href', '').startswith('mailto:')
                            for attrs in links))
        for attrs in links:
            href = attrs.get('href', '')
            if attrs.get('target') == '_blank':
                self.assertEqual(urlsplit(href).scheme, 'https')
                self.assertTrue({'noopener', 'noreferrer'} <=
                                set(attrs.get('rel', '').split()))

    def test_legacy_contact_post_redirects(self):
        response = self.client.post('/submit', data={'message': 'smoke test'})
        self.assertEqual(response.status_code, 303)
        self.assertEqual(response.headers['Location'], '/#contact')

    def test_production_wsgi_entry_point(self):
        from wsgi import app
        self.assertEqual(Client(app, Response).get('/').status_code, 200)
