from fastapi import FastAPI
from app.models.schemas import (
    FeatureRequest,
    GenerateResponse,
    PlanResponse,
    ValidationResponse,
)
from app.agents.planner import generate_plan
from app.agents.coder import generate_code
from app.agents.tester import generate_tests
from app.agents.fixer import fix_code
from app.pipeline.validator import run_validation

app = FastAPI(title="AI Delivery Pipeline Demo")


@app.post("/generate-feature", response_model=GenerateResponse)
def generate_feature(request: FeatureRequest):
    plan_dict = generate_plan(request.feature_request)
    generated_file = generate_code(request.feature_request, plan_dict)
    test_file = generate_tests(request.feature_request, plan_dict)

    initial_validation_dict = run_validation()
    fix_attempted = False

    if initial_validation_dict.get("passed") is False:
        fix_attempted = True
        generated_file = fix_code(
            request.feature_request,
            plan_dict,
            initial_validation_dict.get("test_output", "")
        )

    final_validation_dict = run_validation()

    plan = PlanResponse(
        requirements=plan_dict.get("requirements", []),
        assumptions=plan_dict.get("assumptions", []),
        tasks=plan_dict.get("tasks", []),
    )

    initial_validation = ValidationResponse(
        passed=initial_validation_dict.get("passed", False),
        test_output=initial_validation_dict.get("test_output", "")
    )

    final_validation = ValidationResponse(
        passed=final_validation_dict.get("passed", False),
        test_output=final_validation_dict.get("test_output", "")
    )

    status = "success" if final_validation.passed else "failed_validation"

    return GenerateResponse(
        status=status,
        feature_request=request.feature_request,
        plan=plan,
        generated_file=generated_file,
        test_file=test_file,
        initial_validation=initial_validation,
        fix_attempted=fix_attempted,
        final_validation=final_validation,
    )


@app.get("/health")
def health():
    return {"status": "ok"}