from fastapi.testclient import TestClient
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from .main import app

FIXTURES_BASE = "https://raw.githubusercontent.com/csae8092/"
TEI = f"{FIXTURES_BASE}tei2html/main/fixtures/tei.xml"
XSLT = f"{FIXTURES_BASE}tei2html/main/fixtures/xsl.xsl"


@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())


def test_001_missing_params():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 422


def test_002_with_params():
    with TestClient(app) as client:
        response = client.get(f"/?tei={TEI}&xslt={XSLT}")
        assert response.status_code == 200
