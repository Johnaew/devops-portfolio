from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json()["message"] == "My DevOps portfolio app is running"


def test_health():
	response = client.get("/health")
	assert response.status_code == 200
	assert response.json() == {"status": "healthy"}


def test_metrics():
	client.get("/")
	response = client.get("/metrics")
	assert response.status_code == 200
	assert "http_requests_total" in response.text
