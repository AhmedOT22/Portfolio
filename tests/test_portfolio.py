"""Portfolio integration tests. Run: python -m unittest discover -s tests -v"""
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
        app = create_app()
        app.config["TESTING"] = True
        self.client = Client(app, Response)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.html = response.get_data(as_text=True)
        self.page = PageParser()
        self.page.feed(self.html)

    def test_heading_structure_and_navigation(self):
        elements = self.page.elements
        self.assertEqual(sum(tag == "h1" for tag, _ in elements), 1)
        ids = [attrs["id"] for _, attrs in elements if "id" in attrs]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate IDs")
        for tag, attrs in elements:
            if tag == "a" and attrs.get("href", "").startswith("#"):
                self.assertIn(attrs["href"][1:], ids)

    def test_all_images_and_assets(self):
        for tag, attrs in self.page.elements:
            if tag == "img":
                self.assertTrue(attrs.get("alt"), "Missing image alt text")
            path = attrs.get("src") or attrs.get("href", "")
            if path.startswith("/static/"):
                with self.subTest(path=path):
                    self.assertEqual(self.client.get(path).status_code, 200)
        self.assertIn("ahmed-portrait.webp", self.html)

    def test_curated_projects(self):
        self.assertEqual(
            len([a for tag, a in self.page.elements if tag == "article"]),
            5,
        )
        for project in (
            "Hospital Insights Dashboard",
            "Procurement Contract Analysis",
            "Toronto Air Quality Forecasting",
        ):
            self.assertIn(project, self.html)
        self.assertNotIn("Amazon Sales Analysis", self.html)
        self.assertLess(self.html.index("Toronto Air Quality Forecasting"), self.html.index("Hospital Insights Dashboard"))
        self.assertLess(self.html.index("Hospital Insights Dashboard"), self.html.index("Procurement Contract Analysis"))
        self.assertIn("Private prototype", self.html)
        self.assertIn("27% lower MAE", self.html)
        self.assertIn("Approach, evidence", self.html)
        self.assertIn("Synthetic data", self.html)

    def test_air_quality_live_demo(self):
        self.assertIn("https://air-quality-forecasting1111.streamlit.app/", self.html)
        self.assertIn("Open Toronto Air Quality Forecasting live demo", self.html)
        self.assertIn("Source code", self.html)

    def test_hero_positioning(self):
        self.assertIn("Make sense of data.", self.html)
        self.assertIn("streamlining workflows", self.html)
        self.assertIn("Data Engineering", self.html)
        self.assertIn("Software Development", self.html)
        self.assertIn("ETL/ELT", self.html)
        self.assertIn('href="#work"', self.html)
        self.assertIn('href="#contact"', self.html)
        self.assertNotIn("Download résumé", self.html)
        self.assertNotIn("Download resume", self.html)

    def test_technical_stack(self):
        expected = (
            "Analytics &amp; Business Intelligence",
            "Data Engineering",
            "Machine Learning &amp; Applied AI",
            "Software Development &amp; Deployment",
            "Data Warehousing",
            "Time-Series Forecasting",
            "Git/GitHub Actions",
        )
        for value in expected:
            with self.subTest(value=value):
                self.assertIn(value, self.html)
        self.assertEqual(self.html.count('class="stack-icon"'), 4)
        self.assertEqual(self.html.count('class="stack-card stack-card-primary"'), 1)
        self.assertNotIn('>DEV</span>', self.html)

    def test_external_links_secure(self):
        links = [attrs for tag, attrs in self.page.elements if tag == "a"]
        self.assertTrue(any(a.get("href", "").startswith("mailto:") for a in links))
        for attrs in links:
            if attrs.get("target") == "_blank":
                self.assertEqual(urlsplit(attrs.get("href", "")).scheme, "https")
                self.assertTrue({"noopener", "noreferrer"} <= set(attrs.get("rel", "").split()))

    def test_legacy_submit_redirects_without_storing_data(self):
        response = self.client.post("/submit", data={"message": "test"})
        self.assertEqual(response.status_code, 303)
        self.assertEqual(response.headers["Location"], "/#contact")

    def test_wsgi(self):
        from wsgi import app
        self.assertEqual(Client(app, Response).get("/").status_code, 200)
