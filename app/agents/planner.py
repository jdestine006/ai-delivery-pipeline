import json
from app.utils.llm import call_llm
from app.utils.logging import write_log


def generate_plan(feature_request: str) -> dict:
    prompt = f"""
You are an expert software architect.

Given the following feature request, produce a JSON object with:
- requirements: list of requirements
- assumptions: list of assumptions
- tasks: list of implementation tasks

Return ONLY valid JSON.

Feature request:
{feature_request}
"""

    response = call_llm(prompt)

    write_log("planner_raw_response", {
        "feature_request": feature_request,
        "response": response
    })

    cleaned = response.strip()

    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError:
        parsed = {
            "requirements": [feature_request],
            "assumptions": ["Fallback parser used due to invalid JSON response."],
            "tasks": ["Manually review generated plan"]
        }

    write_log("planner_parsed", parsed)
    return parsed