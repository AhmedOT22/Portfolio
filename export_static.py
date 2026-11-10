"""Export the Flask portfolio to static HTML for CDN hosting.

Run: python export_static.py
Deploy the resulting dist/ directory to Cloudflare Pages or another static host.
"""
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
    # Make absolute Flask static URLs portable to a CDN root.
    html = html.replace('="/static/', '="static/')
    html = html.replace("http://localhost/static/", "static/")
    (output / "index.html").write_text(html, encoding="utf-8")
    copytree(Path(__file__).parent / "static", output / "static")
    print(f"Static portfolio exported to {output.resolve()}")


if __name__ == "__main__":
    export()
