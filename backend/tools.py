from backend.applicant_state import get_applicant_state


GERMANY_DOCUMENTS = [
    {
        "name": "Passport",
        "purpose": "Identity and international travel document",
        "required_for": "Most Germany application and visa processes"
    },
    {
        "name": "Degree Certificate",
        "purpose": "Proof of completed higher education",
        "required_for": "Employment and further education"
    },
    {
        "name": "Academic Transcripts",
        "purpose": "Shows subjects, grades and academic performance",
        "required_for": "University applications and some employment processes"
    },
    {
        "name": "CV",
        "purpose": "Professional and academic profile",
        "required_for": "Employment and vocational applications"
    },
    {
        "name": "Experience Letters",
        "purpose": "Proof of professional experience",
        "required_for": "Employment applications where experience is relevant"
    },
    {
        "name": "Internship Certificates",
        "purpose": "Proof of practical experience",
        "required_for": "Useful for students and early career applicants"
    },
    {
        "name": "Language Certificate",
        "purpose": "Proof of German or English proficiency",
        "required_for": "Depends on university, employer, programme and visa route"
    },
    {
        "name": "Motivation Letter",
        "purpose": "Explains applicant motivation",
        "required_for": "Some universities and employers"
    },
    {
        "name": "Cover Letter",
        "purpose": "Explains suitability for a particular position",
        "required_for": "Often requested by employers"
    },
    {
        "name": "Proof of Qualification Recognition",
        "purpose": "Evidence that a foreign qualification is recognised or comparable where required",
        "required_for": "Depends on profession and immigration pathway"
    },
    {
        "name": "Proof of Financial Resources",
        "purpose": "Shows ability to support yourself where required",
        "required_for": "Certain study and residence routes"
    },
    {
        "name": "Health Insurance",
        "purpose": "Health coverage in Germany",
        "required_for": "Relevant to residence and study processes"
    }
]


GERMANY_PATHWAYS = {
    "employment": {
        "title": "Employment in Germany",
        "steps": [
            "Complete applicant profile",
            "Verify academic qualification",
            "Check whether qualification recognition or comparability evidence is required",
            "Prepare Germany style CV",
            "Prepare cover letter",
            "Prepare degree and transcript documents",
            "Prepare experience and internship evidence",
            "Check German and English language requirements",
            "Find suitable Germany job vacancies",
            "Apply to suitable companies",
            "Prepare for interviews",
            "Check the appropriate residence and visa route"
        ]
    },
    "study": {
        "title": "Study in Germany",
        "steps": [
            "Complete academic profile",
            "Identify target degree and field",
            "Check university admission requirements",
            "Check university entrance qualification",
            "Check language requirements",
            "Prepare degree and transcript documents",
            "Prepare CV if requested",
            "Prepare motivation letter if requested",
            "Apply to suitable universities",
            "Receive admission decision",
            "Check student visa requirements",
            "Arrange health insurance and required financial proof",
            "Complete enrolment"
        ]
    },
    "ausbildung": {
        "title": "Vocational Training in Germany",
        "steps": [
            "Select vocational occupation",
            "Check entry requirements",
            "Check German language requirement",
            "Prepare CV",
            "Prepare certificates",
            "Prepare school qualification documents",
            "Find suitable training companies",
            "Apply for training positions",
            "Attend interviews",
            "Receive training contract",
            "Check visa and residence requirements",
            "Prepare for relocation"
        ]
    }
}


GERMANY_COMPANIES = [
    {
        "name": "SAP",
        "sector": "Software and Enterprise Technology",
        "relevant_roles": [
            "Software Engineering",
            "Artificial Intelligence",
            "Machine Learning",
            "Data",
            "Cloud",
            "Technology Consulting"
        ]
    },
    {
        "name": "Siemens",
        "sector": "Technology and Engineering",
        "relevant_roles": [
            "Artificial Intelligence",
            "Software Engineering",
            "Automation",
            "Data",
            "Digital Industries",
            "Research and Development"
        ]
    },
    {
        "name": "Bosch",
        "sector": "Engineering and Technology",
        "relevant_roles": [
            "Artificial Intelligence",
            "Machine Learning",
            "Software Engineering",
            "Automotive Technology",
            "Data Science",
            "Research and Development"
        ]
    },
    {
        "name": "BMW Group",
        "sector": "Automotive and Technology",
        "relevant_roles": [
            "Artificial Intelligence",
            "Data Science",
            "Software Engineering",
            "Autonomous Systems",
            "Research and Development"
        ]
    },
    {
        "name": "Mercedes Benz",
        "sector": "Automotive and Technology",
        "relevant_roles": [
            "Artificial Intelligence",
            "Machine Learning",
            "Software Engineering",
            "Data Science",
            "Autonomous Driving"
        ]
    },
    {
        "name": "Volkswagen Group",
        "sector": "Automotive and Mobility",
        "relevant_roles": [
            "Artificial Intelligence",
            "Software Engineering",
            "Data",
            "Mobility Technology",
            "Research and Development"
        ]
    },
    {
        "name": "Deutsche Telekom",
        "sector": "Telecommunications and Technology",
        "relevant_roles": [
            "Software Engineering",
            "Artificial Intelligence",
            "Data",
            "Cloud",
            "Cybersecurity"
        ]
    }
]


GERMANY_UNIVERSITIES = [
    {
        "name": "Technical University of Munich",
        "focus": "Engineering, Computer Science, Artificial Intelligence and Technology"
    },
    {
        "name": "RWTH Aachen University",
        "focus": "Engineering, Computer Science, Technology and Research"
    },
    {
        "name": "Karlsruhe Institute of Technology",
        "focus": "Computer Science, Engineering, Technology and Research"
    },
    {
        "name": "TU Berlin",
        "focus": "Computer Science, Engineering and Technology"
    },
    {
        "name": "University of Stuttgart",
        "focus": "Engineering, Computer Science and Technology"
    },
    {
        "name": "Saarland University",
        "focus": "Computer Science and Artificial Intelligence"
    }
]


def inspect_applicant():
    state = get_applicant_state()

    return {
        "success": True,
        "tool": "inspect_applicant",
        "result": {
            "status": "completed",
            "applicant": state
        }
    }


def analyze_missing_documents():

    state = get_applicant_state()

    uploaded_documents = state.get("documents", [])

    uploaded_names = []

    for document in uploaded_documents:
        if isinstance(document, dict):
            uploaded_names.append(
                document.get("filename", "").lower()
            )

    missing = []

    for document in GERMANY_DOCUMENTS:

        name = document["name"].lower()

        found = False

        for uploaded_name in uploaded_names:

            if (
                "passport" in name
                and "passport" in uploaded_name
            ):
                found = True

            elif (
                "degree" in name
                and "degree" in uploaded_name
            ):
                found = True

            elif (
                "transcript" in name
                and (
                    "transcript" in uploaded_name
                    or "grade" in uploaded_name
                    or "marks" in uploaded_name
                )
            ):
                found = True

            elif (
                "cv" in name
                and "resume" in uploaded_name
            ):
                found = True

            elif (
                "experience" in name
                and "experience" in uploaded_name
            ):
                found = True

            elif (
                "internship" in name
                and "intern" in uploaded_name
            ):
                found = True

            elif (
                "language" in name
                and (
                    "ielts" in uploaded_name
                    or "german" in uploaded_name
                    or "language" in uploaded_name
                )
            ):
                found = True

        if not found:
            missing.append(document)

    return {
        "success": True,
        "tool": "analyze_missing_documents",
        "result": {
            "status": "completed",
            "uploaded_document_count": len(uploaded_documents),
            "missing_documents": missing
        }
    }


def evaluate_qualification():

    state = get_applicant_state()

    education = state.get("education", "")
    degree = state.get("degree", "")
    field = state.get("field", "")
    experience = state.get("experience", "")
    target = state.get("target", "")
    german = state.get("german_level", "")
    english = state.get("english_level", "")

    matches = []
    gaps = []
    recommendations = []

    if education:
        matches.append(
            "Higher education information is available."
        )

    if degree:
        matches.append(
            "Degree information is available."
        )

    if field:
        matches.append(
            "Field of study is " + str(field) + "."
        )

    if english:
        matches.append(
            "English language level is " + str(english) + "."
        )

    if german:
        matches.append(
            "German language level is " + str(german) + "."
        )

    if not education:
        gaps.append(
            "Complete higher education information."
        )

    if not degree:
        gaps.append(
            "Degree details and final qualification evidence."
        )

    if not experience:
        gaps.append(
            "Professional or internship experience."
        )

    if not target:
        gaps.append(
            "Target Germany pathway or occupation."
        )

    if target:
        recommendations.append(
            "Check the qualification requirements for the selected Germany occupation."
        )

    recommendations.append(
        "Check whether the foreign academic qualification needs recognition or comparability evidence."
    )

    recommendations.append(
        "Check the German and English language requirements of each selected employer or university."
    )

    if gaps:
        status = "requires_additional_information"
    else:
        status = "completed"

    return {
        "success": True,
        "tool": "evaluate_qualification",
        "result": {
            "status": status,
            "matches": matches,
            "gaps": gaps,
            "recommendations": recommendations,
            "germany_note": (
                "Qualification requirements depend on the occupation, university, "
                "employer and immigration pathway."
            )
        }
    }


def get_germany_pathway():

    state = get_applicant_state()

    target = str(
        state.get("target", "")
    ).lower()

    if (
        "study" in target
        or "master" in target
        or "university" in target
    ):
        pathway = "study"

    elif (
        "ausbildung" in target
        or "training" in target
        or "vocational" in target
    ):
        pathway = "ausbildung"

    else:
        pathway = "employment"

    data = GERMANY_PATHWAYS[pathway]

    return {
        "success": True,
        "tool": "get_germany_pathway",
        "result": {
            "pathway": pathway,
            "title": data["title"],
            "steps": data["steps"]
        }
    }


def get_germany_companies():

    state = get_applicant_state()

    field = str(
        state.get("field", "")
    ).lower()

    relevant = []

    for company in GERMANY_COMPANIES:

        roles = " ".join(
            company["relevant_roles"]
        ).lower()

        if (
            not field
            or "artificial intelligence" in roles
            or "machine learning" in roles
            or "computer" in field
            or "software" in field
            or "ai" in field
        ):
            relevant.append(company)

    return {
        "success": True,
        "tool": "get_germany_companies",
        "result": {
            "companies": relevant
        }
    }


def get_germany_universities():

    return {
        "success": True,
        "tool": "get_germany_universities",
        "result": {
            "universities": GERMANY_UNIVERSITIES
        }
    }


def generate_next_steps():

    state = get_applicant_state()

    steps = []

    if not state.get("experience"):
        steps.append(
            "Add professional, internship, project or practical experience."
        )

    steps.append(
        "Complete Germany document verification."
    )

    steps.append(
        "Check academic qualification recognition or comparability requirements."
    )

    steps.append(
        "Check German language requirements for the selected pathway."
    )

    steps.append(
        "Prepare a Germany focused CV."
    )

    steps.append(
        "Select suitable Germany universities or companies."
    )

    steps.append(
        "Check the specific admission, employment and visa requirements."
    )

    return {
        "success": True,
        "tool": "generate_next_steps",
        "result": {
            "status": "completed",
            "steps": steps
        }
    }


def generate_cv():

    state = get_applicant_state()

    return {
        "success": True,
        "tool": "generate_cv",
        "result": {
            "status": "completed",
            "applicant": state
        }
    }
