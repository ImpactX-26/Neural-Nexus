from backend.applicant_state import get_applicant_state, update_state
from backend.ai_service import ask_ai


def generate_cv(data):

    state = get_applicant_state()

    applicant = state["applicant"]

    target_role = data.get(
        "target_role",
        applicant.get("target", "")
    )

    system_prompt = """
You are the LearnoryX professional CV generation agent.

Create a structured, factual CV for an applicant targeting Germany.

Do not invent:
- degrees
- companies
- job titles
- achievements
- skills
- certifications
- dates

Only use information available in the applicant profile and verified documents.

Return a clean professional CV structure.
"""

    user_prompt = f"""
Applicant profile:

{applicant}

Verified documents:

{state["documents"]}

Target role:

{target_role}

Target country:

{data.get("target_country", "Germany")}

Language:

{data.get("language", "English")}
"""

    response = ask_ai(
        system_prompt,
        user_prompt
    )

    if response["success"]:

        content = response["content"]

    else:

        content = generate_fallback_cv(
            applicant,
            target_role
        )

    result = {
        "generated": True,
        "target_role": target_role,
        "content": content
    }

    update_state(
        "cv",
        result
    )

    return result


def generate_fallback_cv(
    applicant,
    target_role
):

    return f"""
PROFESSIONAL PROFILE

Name: {applicant.get("name", "")}

Email: {applicant.get("email", "")}

Phone: {applicant.get("phone", "")}

Education:
{applicant.get("education", "")}

Degree:
{applicant.get("degree", "")}

Field:
{applicant.get("field", "")}

Experience:
{applicant.get("experience", "")}

Target Role:
{target_role}

Languages:
English: {applicant.get("english_level", "")}
German: {applicant.get("german_level", "")}
"""