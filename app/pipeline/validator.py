import subprocess
from app.utils.logging import write_log

def run_validation() -> dict:
    try:
        result = subprocess.run(["pytest", "generated/tests", "-q"], 
                                capture_output=True, 
                                text=True,
                                timeout=20
                                )
        
        passed = result.returncode == 0
        output = (result.stdout or "") + "\n" + (result.stderr or "")

        response = {
            "passed": passed,
            "test_output": output.strip()
        }

        write_log("validator_result", response)
        return response
    
    except subprocess.TimeoutExpired:
        response = {
            "passed": False,
            "test_output": "Validation timed out."
        }
        write_log("validator_result", response)
        return response