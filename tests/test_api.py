# tests/test_api.py
import pytest
import base64
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

@ pytest.mark.asyncio
async def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["up"] is True

@ pytest.mark.asyncio
async def test_search_missing_image():
    response = client.post("/search", json={})
    assert response.status_code == 400

@ pytest.mark.asyncio
async def test_search_valid_image():
    # Minimal 1x1 transparent PNG in base64
    img_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
    response = client.post("/search", json={"image": img_b64})
    assert response.status_code == 200