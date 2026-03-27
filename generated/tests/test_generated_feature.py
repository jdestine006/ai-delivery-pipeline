from fastapi.testclient import TestClient
from generated.code.generated_feature import app

client = TestClient(app)

def test_create_inquiry_success():
    response = client.post("/inquiries", json={
        "message": "hello"
        })
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "received"
    assert body["message"] == "hello"
