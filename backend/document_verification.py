import re


def verify_document(
    filename,
    extracted_text
):

    text = extracted_text.lower()

    indicators = {
        "name_detected": False,
        "institution_detected": False,
        "qualification_detected": False,
        "date_detected": False,
        "document_content_detected": len(text.strip()) > 50
    }

    if re.search(
        r"\b(name|student|candidate|applicant)\b",
        text
    ):
        indicators["name_detected"] = True

    if re.search(
        r"\b(university|college|institute|school)\b",
        text
    ):
        indicators["institution_detected"] = True

    if re.search(
        r"\b(bachelor|master|degree|diploma|certificate|b\.tech|bca|mca|bsc|msc)\b",
        text
    ):
        indicators["qualification_detected"] = True

    if re.search(
        r"\b(19|20)\d{2}\b",
        text
    ):
        indicators["date_detected"] = True

    detected_count = sum(
        1 for value in indicators.values()
        if value
    )

    if detected_count >= 4:
        status = "strong_match"

    elif detected_count >= 2:
        status = "partial_match"

    else:
        status = "needs_review"

    return {
        "status": status,
        "indicators": indicators,
        "confidence": round(
            detected_count / len(indicators),
            2
        ),
        "message": (
            "Document contains multiple expected academic or professional indicators."
            if status == "strong_match"
            else "Document requires additional verification."
        )
    }