from pydantic import BaseModel
from typing import List

class FeatureRequest(BaseModel):
    feature_request: str

class PlanResponse(BaseModel):
    requirements: List[str]
    assumptions: List[str]
    tasks: List[str]

class ValidationResponse(BaseModel):
    passed: bool
    test_output: str

class GenerateResponse(BaseModel):
    plan: PlanResponse
    feature_request: str
    status: str
    generated_file: str
    test_file: str
    initial_validation: ValidationResponse
    fix_attempted: bool
    final_validation: ValidationResponse