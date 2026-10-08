from backend.applicant_state import get_applicant_state

from backend.tools import (
    inspect_applicant,
    analyze_missing_documents,
    evaluate_qualification,
    get_germany_pathway,
    get_germany_companies,
    get_germany_universities,
    generate_next_steps
)


MAX_STEPS = 7


def clean_text(value):

    if value is None:
        return ""

    text = str(value)

    symbols = [
        "*", "_", "`", "#", "~",
        "•", "●", "▪", "◦",
        "◆", "◇", "▶", "►",
        "✓", "✔", "✦", "✧",
        "★", "☆", "→", "←",
        "↑", "↓"
    ]

    for symbol in symbols:
        text = text.replace(symbol, "")

    return text.strip()


def build_response(results):
    """
    Build a clean, readable Germany applicant analysis.
    Adds proper spacing between sections and individual answers.
    """

    sections = []

    # ========================================================
    # TITLE
    # ========================================================

    sections.append(
        "Germany Applicant Analysis Completed"
    )

    # ========================================================
    # STEP 1
    # ========================================================

    applicant = results.get("inspect_applicant", {})

    profile_lines = [
        "Step 1: Applicant Profile",
        "",
        f"Name: {applicant.get('name', 'Not provided')}",
        "",
        f"Education: {applicant.get('education', 'Not provided')}",
        "",
        f"Degree: {applicant.get('degree', 'Not provided')}",
        "",
        f"Field: {applicant.get('field', 'Not provided')}",
        "",
        f"Target: {applicant.get('target', 'Not provided')}",
        "",
        f"German level: {applicant.get('german_level', 'Not provided')}",
        "",
        f"English level: {applicant.get('english_level', 'Not provided')}",
    ]

    sections.append("\n".join(profile_lines))

    # ========================================================
    # STEP 2
    # ========================================================

    qualification = results.get(
        "evaluate_qualification",
        {}
    )

    qualification_lines = [
        "Step 2: Qualification Assessment",
        ""
    ]

    if isinstance(qualification, dict):

        available = qualification.get(
            "available"
        )

        if available:
            qualification_lines.append(
                "Available: Higher education information is available."
            )
            qualification_lines.append("")

        missing = qualification.get(
            "missing",
            []
        )

        if isinstance(missing, list):

            for item in missing:
                qualification_lines.append(
                    f"Missing: {item}"
                )
                qualification_lines.append("")

        recommendations = qualification.get(
            "recommendations",
            []
        )

        if isinstance(recommendations, list):

            for item in recommendations:
                qualification_lines.append(
                    f"Recommendation: {item}"
                )
                qualification_lines.append("")

    sections.append(
        "\n".join(qualification_lines).strip()
    )

    # ========================================================
    # STEP 3
    # ========================================================

    documents = results.get(
        "analyze_missing_documents",
        {}
    )

    document_lines = [
        "Step 3: Germany Documents",
        ""
    ]

    if isinstance(documents, dict):

        document_list = documents.get(
            "documents",
            []
        )

        if document_list:

            for document in document_list:

                if isinstance(document, dict):

                    name = document.get(
                        "name",
                        "Document"
                    )

                    purpose = document.get(
                        "purpose",
                        ""
                    )

                    required_for = document.get(
                        "required_for",
                        ""
                    )

                    document_lines.append(
                        f"Document: {name}"
                    )

                    if purpose:
                        document_lines.append(
                            f"Purpose: {purpose}"
                        )

                    if required_for:
                        document_lines.append(
                            f"Required for: {required_for}"
                        )

                    document_lines.append("")

                else:

                    document_lines.append(
                        f"Document: {document}"
                    )

                    document_lines.append("")

    sections.append(
        "\n".join(document_lines).strip()
    )

    # ========================================================
    # STEP 4
    # ========================================================

    pathway = results.get(
        "get_germany_pathway",
        {}
    )

    pathway_lines = [
        "Step 4: Germany Pathway",
        ""
    ]

    if isinstance(pathway, dict):

        pathway_name = pathway.get(
            "pathway",
            "Germany pathway"
        )

        pathway_lines.append(
            f"Pathway: {pathway_name}"
        )

        pathway_lines.append("")

        steps = pathway.get(
            "steps",
            []
        )

        for index, step in enumerate(
            steps,
            start=1
        ):

            pathway_lines.append(
                f"Pathway step {index}: {step}"
            )

            pathway_lines.append("")

    sections.append(
        "\n".join(pathway_lines).strip()
    )

    # ========================================================
    # STEP 5
    # ========================================================

    universities = results.get(
        "get_germany_universities",
        {}
    )

    university_lines = [
        "Step 5: Germany Universities",
        ""
    ]

    if isinstance(universities, dict):

        university_list = universities.get(
            "universities",
            []
        )

        for university in university_list:

            if isinstance(university, dict):

                name = university.get(
                    "name",
                    "University"
                )

                focus = university.get(
                    "focus",
                    ""
                )

                university_lines.append(
                    f"{name}"
                )

                if focus:
                    university_lines.append(
                        f"Focus: {focus}"
                    )

                university_lines.append("")

            else:

                university_lines.append(
                    str(university)
                )

                university_lines.append("")

    sections.append(
        "\n".join(university_lines).strip()
    )

    # ========================================================
    # STEP 6
    # ========================================================

    companies = results.get(
        "get_germany_companies",
        {}
    )

    company_lines = [
        "Step 6: Germany Companies",
        ""
    ]

    if isinstance(companies, dict):

        company_list = companies.get(
            "companies",
            []
        )

        for company in company_list:

            if isinstance(company, dict):

                name = company.get(
                    "name",
                    "Company"
                )

                sector = company.get(
                    "sector",
                    ""
                )

                roles = company.get(
                    "relevant_roles",
                    []
                )

                company_lines.append(
                    f"{name}"
                )

                if sector:
                    company_lines.append(
                        f"Sector: {sector}"
                    )

                if roles:

                    if isinstance(roles, list):

                        company_lines.append(
                            "Relevant roles:"
                        )

                        for role in roles:

                            company_lines.append(
                                f"  {role}"
                            )

                    else:

                        company_lines.append(
                            f"Relevant roles: {roles}"
                        )

                company_lines.append("")

    sections.append(
        "\n".join(company_lines).strip()
    )

    # ========================================================
    # STEP 7
    # ========================================================

    next_steps = results.get(
        "generate_next_steps",
        {}
    )

    next_lines = [
        "Step 7: Next Actions",
        ""
    ]

    if isinstance(next_steps, dict):

        actions = next_steps.get(
            "actions",
            []
        )

        for index, action in enumerate(
            actions,
            start=1
        ):

            next_lines.append(
                f"Next action {index}: {action}"
            )

            next_lines.append("")

    sections.append(
        "\n".join(next_lines).strip()
    )

    # ========================================================
    # FINAL RESPONSE
    # ========================================================

    return "\n\n".join(
        section.strip()
        for section in sections
        if section and section.strip()
    )


def run_agent_loop(message=""):

    trace = []
    results = {}

    actions = [
        (
            "inspect_applicant",
            inspect_applicant
        ),
        (
            "analyze_missing_documents",
            analyze_missing_documents
        ),
        (
            "evaluate_qualification",
            evaluate_qualification
        ),
        (
            "get_germany_pathway",
            get_germany_pathway
        ),
        (
            "get_germany_companies",
            get_germany_companies
        ),
        (
            "get_germany_universities",
            get_germany_universities
        ),
        (
            "generate_next_steps",
            generate_next_steps
        )
    ]

    for step_number, (
        action_name,
        action_function
    ) in enumerate(
        actions,
        start=1
    ):

        trace.append({
            "step": step_number,
            "status": "selected",
            "action": action_name
        })

        try:

            result = action_function()

        except Exception as error:

            result = {
                "success": False,
                "message": str(error)
            }

        trace.append({
            "step": step_number,
            "status": "completed",
            "action": action_name
        })

        if not result.get("success", False):

            trace.append({
                "step": step_number,
                "status": "failed",
                "action": action_name
            })

            break

        data = result.get(
            "result",
            {}
        )

        if action_name == "inspect_applicant":

            results["applicant"] = data.get(
                "applicant",
                {}
            ).get(
                "applicant",
                data.get("applicant", {})
            )

        elif action_name == "analyze_missing_documents":

            results["documents"] = data

        elif action_name == "evaluate_qualification":

            results["qualification"] = data

        elif action_name == "get_germany_pathway":

            results["pathway"] = data

        elif action_name == "get_germany_companies":

            results["companies"] = data

        elif action_name == "get_germany_universities":

            results["universities"] = data

        elif action_name == "generate_next_steps":

            results["next_steps"] = data


    answer = build_response(results)

    return {
        "agent_status": "completed",
        "message": clean_text(message),
        "answer": clean_text(answer),
        "result": results,
        "next_action": (
            "Complete the missing documents and qualification requirements, "
            "then continue with Germany applications."
        ),
        "trace": trace,
        "state": get_applicant_state()
    }