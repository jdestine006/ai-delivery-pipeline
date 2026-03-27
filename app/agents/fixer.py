from pathlib import Path
from textwrap import dedent
from app.utils.logging import write_log

CODE_DIR = Path("generated/code")
CODE_DIR.mkdir(parents=True, exist_ok=True)

def fix_code(feature_request: str, plan: dict, test_output: str) -> str:
    fixed_code = dedent('''from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InquiryRequest(BaseModel):
    message: str

@app.post("/inquiries")
def create_inquiry(request: InquiryRequest):
    return {"status": "received", "message": request.message}
''')

    file_path = CODE_DIR / "generated_feature.py"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(fixed_code)

    write_log("fixer_output_file", {
        "feature_request": feature_request,
        "plan": plan,
        "test_output": test_output,
        "file_path": str(file_path)
    })

    return str(file_path)