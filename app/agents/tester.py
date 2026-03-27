from pathlib import Path
from textwrap import dedent
from app.utils.logging import write_log

TEST_DIR = Path('generated/tests')
TEST_DIR.mkdir(parents=True, exist_ok=True)

def generate_tests(feature_request: str, plan: dict) -> str:
    test_code = dedent('''\
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
    ''')

    file_path = TEST_DIR / "test_generated_feature.py"

    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(test_code)

    write_log("tester_output_file", {
        "feature_request": feature_request,
        "plan": plan,
        "test_file": str(file_path)
    })

    return str(file_path)