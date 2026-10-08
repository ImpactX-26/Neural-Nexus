from backend.applicant_state import get_applicant_state


def verify_agent_result(result):
    state = get_applicant_state()

    checks = {
        "state_available": state is not None,
        "result_available": result is not None,
        "applicant_state_valid": "applicant" in state,
        "documents_state_valid": "documents" in state,
        "agent_state_valid": "agent" in state,
        "status_updated": bool(state.get("agent_status"))
    }

    passed = sum(1 for value in checks.values() if value)
    confidence = round(passed / len(checks), 2)

    return {
        "verified": passed == len(checks),
        "confidence": confidence,
        "checks": checks
    }