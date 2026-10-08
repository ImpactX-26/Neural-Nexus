from backend.applicant_state import get_applicant_state, update_state


def generate_next_steps():

    state = get_applicant_state()

    applicant = state["applicant"]
    documents = state["documents"]
    qualification = state["qualification"]

    steps = []

    if not applicant.get("name"):
        steps.append({
            "priority": "high",
            "action": "Complete applicant profile",
            "reason": "Basic identity information is missing."
        })

    if not applicant.get("education"):
        steps.append({
            "priority": "high",
            "action": "Add education details",
            "reason": "Education is required for pathway evaluation."
        })

    if len(documents) == 0:
        steps.append({
            "priority": "high",
            "action": "Upload academic or professional documents",
            "reason": "Documents are required for evidence-based verification."
        })

    elif any(
        document["verification"]["status"] != "strong_match"
        for document in documents
    ):
        steps.append({
            "priority": "medium",
            "action": "Review document verification",
            "reason": "One or more uploaded documents require additional review."
        })

    if qualification["status"] == "not_evaluated":
        steps.append({
            "priority": "high",
            "action": "Run qualification evaluation",
            "reason": "The applicant pathway has not yet been evaluated."
        })

    if not applicant.get("target"):
        steps.append({
            "priority": "medium",
            "action": "Select Germany pathway",
            "reason": "Choose study, vocational training, or employment."
        })

    if not applicant.get("german_level"):
        steps.append({
            "priority": "medium",
            "action": "Add German language level",
            "reason": "Language requirements can vary across Germany pathways."
        })

    if not steps:
        steps.append({
            "priority": "low",
            "action": "Continue with detailed application preparation",
            "reason": "The core applicant information is available."
        })

    update_state(
        "next_steps",
        steps
    )

    return steps