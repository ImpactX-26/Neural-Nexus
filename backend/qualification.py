from backend.applicant_state import update_state


def evaluate_qualification(data):

    target_type = data.get(
        "target_type",
        ""
    ).lower()

    target_name = data.get(
        "target_name",
        ""
    )

    field = data.get(
        "field",
        ""
    )

    education = data.get(
        "education",
        ""
    )

    experience = data.get(
        "experience",
        ""
    )

    german = data.get(
        "german_level",
        ""
    )

    english = data.get(
        "english_level",
        ""
    )

    matches = []
    gaps = []
    recommendations = []

    if education:
        matches.append(
            "Education information is available."
        )
    else:
        gaps.append(
            "Education information is missing."
        )

    if field:
        matches.append(
            f"Field information available: {field}."
        )
    else:
        gaps.append(
            "Academic or professional field is missing."
        )

    if experience:
        matches.append(
            "Experience information is available."
        )
    else:
        gaps.append(
            "Experience information should be added."
        )

    if english:
        matches.append(
            f"English level recorded as {english}."
        )
    else:
        gaps.append(
            "English proficiency has not been provided."
        )

    if target_type in ["study", "vocational training", "employment"]:

        recommendations.append(
            f"Research eligibility requirements for the selected {target_type} pathway."
        )

    if not german:
        recommendations.append(
            "Add German language information because it can be relevant to Germany-based pathways."
        )

    result = {
        "target_type": target_type,
        "target_name": target_name,
        "status": "requires_additional_information"
        if gaps else "ready_for_detailed_review",
        "matches": matches,
        "gaps": gaps,
        "recommendations": recommendations
    }

    update_state(
        "qualification",
        result
    )

    return result