from backend.applicant_state import update_state, get_applicant_state


def update_profile(data):

    current = get_applicant_state()["applicant"]

    cleaned = {}

    for key, value in data.items():

        if value is not None and str(value).strip():

            cleaned[key] = str(value).strip()

    current.update(cleaned)

    update_state(
        "applicant",
        current
    )

    return current