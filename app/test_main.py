from fastapi.testclient import TestClient
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from .main import app


@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())


def test_001_missing_params():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 422


def test_002_with_params():
    with TestClient(app) as client:
        response = client.get("/?tei=https://id.acdh.oeaw.ac.at/thun/editions/kaiser-an-thun-07-15-a3-xxi-d634f.xml&xslt=https://tei4arche.acdh-dev.oeaw.ac.at/xsl/thun2arche.xsl")
        assert response.status_code == 200
