"""Export the Flask portfolio to static HTML for CDN hosting.

Run: python export_static.py
Deploy the resulting dist/ directory to Cloudflare Pages or another static host.
"""
import os
from pathlib import Path
from shutil import copytree, rmtree

from werkzeug.test import Client
from werkzeug.wrappers import Response

from app import create_app


def export(output_dir="dist"):
    output = Path(output_dir)
    if output.exists():
        rmtree(output)
    output.mkdir(parents=True)
    app = create_app()
    app.config["TESTING"] = True
    client = Client(app, Response)
    response = client.get("/")
    if response.status_code != 200:
        raise RuntimeError(f"Homepage returned {response.status_code}")
    html = response.get_data(as_text=True)
    # Root-relative assets work at any pages.dev or custom domain.
    # Social preview image URLs must remain absolute for sharing services.
    site_url = os.environ.get("CF_PAGES_URL", "").rstrip("/")
    if site_url:
        html = html.replace("http://localhost/static/", f"{site_url}/static/")
    else:
        html = html.replace("http://localhost/static/", "https://raw.githubusercontent.com/AhmedOT22/Portfolio/main/static/")
    (output / "index.html").write_text(html, encoding="utf-8")
    copytree(Path(__file__).parent / "static", output / "static")
    print(f"Static portfolio exported to {output.resolve()}")


if __name__ == "__main__":
    export()
