from backend.applicant_state import get_applicant_state


def determine_next_action():
    state = get_applicant_state()
    applicant = state.get("applicant", {})
    documents = state.get("documents", [])
    qualification = state.get("qualification", {})
    cv = state.get("cv", {})

    if not applicant.get("name"):
        return {
            "action": "collect_profile",
            "reason": "Applicant identity information is incomplete.",
            "current_stage": "profile"
        }

    if not applicant.get("education"):
        return {
            "action": "collect_education",
            "reason": "Education information is required.",
            "current_stage": "education"
        }

    if not applicant.get("target"):
        return {
            "action": "select_pathway",
            "reason": "Applicant has not selected a Germany pathway.",
            "current_stage": "pathway"
        }

    if len(documents) == 0:
        return {
            "action": "request_documents",
            "reason": "No applicant documents are available for verification.",
            "current_stage": "documents"
        }

    unverified = [
        document
        for document in documents
        if document.get("verification", {}).get("status") != "strong_match"
    ]

    if unverified:
        return {
            "action": "verify_documents",
            "reason": "One or more documents require additional verification.",
            "current_stage": "verification"
        }

    if qualification.get("status") in ["not_evaluated", "requires_additional_information"]:
        return {
            "action": "evaluate_qualification",
            "reason": "Applicant qualification has not been evaluated or needs additional requirements.",
            "current_stage": "qualification"
        }

    if not cv.get("generated"):
        return {
            "action": "prepare_cv",
            "reason": "Applicant has not yet generated a target-specific CV.",
            "current_stage": "cv"
        }

    if not state.get("next_steps"):
        return {
            "action": "generate_next_steps",
            "reason": "Core applicant processing is complete and next steps are ready.",
            "current_stage": "next_steps"
        }

    return {
        "action": "complete_journey",
        "reason": "All major applicant journey requirements have been satisfied.",
        "current_stage": "complete"
    }