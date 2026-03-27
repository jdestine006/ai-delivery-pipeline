from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InquiryRequest(BaseModel):
    message: str

@app.post("/inquiries")
def create_inquiry(request: InquiryRequest):
    return {"status": "received", "message": request.message}
