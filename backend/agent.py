from backend.orchestrator import run_agent_loop


def run_agent(message=""):

    try:

        result = run_agent_loop(message)

        answer = result.get("answer", "")

        if not answer:
            answer = (
                "LearnoryX completed the analysis but did not "
                "generate a visible response."
            )

        return {
            "success": True,
            "agent_status": "completed",
            "decision": "Germany applicant analysis completed",
            "action": "Analyze applicant and determine next steps",
            "result": answer,
            "answer": answer,
            "message": answer,
            "next_action": result.get(
                "next_action",
                "Continue with the next applicant requirement."
            ),
            "state": result.get("state", {}),
            "trace": result.get("trace", [])
        }

    except Exception as error:

        error_message = str(error)

        return {
            "success": False,
            "agent_status": "error",
            "decision": "Agent execution failed",
            "action": "Error handling",
            "result": "",
            "answer": (
                "LearnoryX could not complete the request.\n\n"
                "Backend error: " + error_message
            ),
            "message": error_message,
            "next_action": "Check the backend terminal for the error.",
            "state": {},
            "trace": []
        }