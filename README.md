# AI Delivery Pipeline (Self-Healing Workflow)

This project explores how AI can be used beyond simple code generation by introducing validation, feedback, and remediation into the delivery lifecycle.

## Overview

Instead of stopping at "generate code", this system implements a closed-loop pipeline:

Feature Request → Plan → Code → Tests → Validation → Fix (if needed) → Re-validate

The goal is to simulate a simplified **AI-driven delivery system** with basic self-healing behavior.

---

## Key Concepts

- **Agent-based architecture**
  - Planner
  - Code generator
  - Test generator
  - Validator
  - Fixer

- **Validation as a decision point**
  - Not just reporting success/failure
  - Drives system behavior

- **Remediation loop**
  - Automatically attempts to fix failing outputs
  - Re-runs validation before returning result

---

## Example Output

```json
{
  "initial_validation": { "passed": false },
  "fix_attempted": true,
  "final_validation": { "passed": true },
  "status": "success"
}

```

## Tech Stack

```
  Python
  FastAPI
  Pytest (validation)
  OpenAI API (structured planning)
  Agent-based architecture
```

## How to Run Program
```
pip install -r requirements.txt
uvicorn app.main:app --reload 
```

## Open
```
http://localhost:8000/docs

```