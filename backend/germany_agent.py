import json
import re

from gemma_service import ask_gemma
from jobs_service import search_germany_jobs


def _clean_json_from_ai(raw_text):
    if raw_text is None:
        return "{}"

    text = str(raw_text).strip()
    text = text.replace("```json", "").replace("```", "").strip()
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)
    return text


async def analyze_applicant(profile):
    prompt = f"""
You are the Germany Applicant Agent of LearnoryX.

Analyze the following applicant:

{json.dumps(profile, indent=2)}

The applicant wants to study, work, or pursue vocational opportunities in Germany.

Determine:
1. Suitable job roles
2. Job-search keywords
3. Important skills
4. Missing skills
5. German language requirement
6. Qualification gaps
7. Recommended next steps

Return ONLY valid JSON.

Format:
{{
    "recommended_roles": [],
    "search_keywords": [],
    "skills": [],
    "missing_skills": [],
    "language_requirement": "",
    "qualification_gaps": [],
    "next_steps": []
}}
"""

    try:
        result = await ask_gemma(prompt)
        cleaned = _clean_json_from_ai(result)
        parsed = json.loads(cleaned)

        return {
            "recommended_roles": parsed.get("recommended_roles", []),
            "search_keywords": parsed.get("search_keywords", []),
            "skills": parsed.get("skills", []),
            "missing_skills": parsed.get("missing_skills", []),
            "language_requirement": parsed.get("language_requirement", ""),
            "qualification_gaps": parsed.get("qualification_gaps", []),
            "next_steps": parsed.get("next_steps", []),
        }
    except Exception as error:
        print(f"[LearnoryX] Gemma applicant analysis parse failed: {error}")
        return {
            "recommended_roles": [],
            "search_keywords": [],
            "skills": [],
            "missing_skills": [],
            "language_requirement": "",
            "qualification_gaps": [],
            "next_steps": [],
            "raw_response": str(result) if 'result' in locals() else ""
        }


async def search_jobs_for_applicant(profile):
    analysis = await analyze_applicant(profile)
    keywords = analysis.get("search_keywords", []) or analysis.get("recommended_roles", [])
    location = profile.get("preferred_location") or profile.get("location") or "Germany"

    all_jobs = []

    for keyword in keywords[:5]:
        try:
            result = await search_germany_jobs(keyword=keyword, location=location, size=10)
            jobs = result.get("stellenangebote", []) if isinstance(result, dict) else []

            for job in jobs:
                if isinstance(job, dict):
                    job["_learnoryx_keyword"] = keyword
                all_jobs.append(job)

        except Exception as error:
            print(f"[LearnoryX] Job search failed for '{keyword}': {error}")

    unique_jobs = {}
    for job in all_jobs:
        reference = (job.get("refnr") or job.get("referenznummer") or job.get("titel") or str(job)) if isinstance(job, dict) else str(job)
        unique_jobs[reference] = job

    jobs = list(unique_jobs.values())
    return analysis, jobs


async def match_jobs_to_applicant(profile, analysis, jobs):
    if not jobs:
        return {"recommendations": []}

    job_slice = jobs[:10]
    prompt = f"""
You are the Germany Applicant Agent of LearnoryX.

Compare the applicant profile to the Germany job results and return only valid JSON.

Applicant profile:
{json.dumps(profile, indent=2)}

Applicant analysis:
{json.dumps(analysis, indent=2)}

Jobs to compare:
{json.dumps(job_slice, indent=2, default=str)}

Return JSON format:
{{
  "recommendations": [
    {{
      "title": "",
      "company": "",
      "location": "",
      "match_score": 0,
      "matching_skills": [],
      "missing_skills": [],
      "recommendation": ""
    }}
  ]
}}

Rules:
- Only use actual job information returned by the jobs API.
- If company, title, or location is missing, use "Not provided".
- Match scores must be integers from 0 to 100.
- Keep recommendations concise and factual.
"""

    try:
        response = await ask_gemma(prompt)
        cleaned = _clean_json_from_ai(response)
        parsed = json.loads(cleaned)
        recommendations = parsed.get("recommendations", [])
        return {"recommendations": recommendations}
    except Exception as exc:
        print(f"[LearnoryX] Job matching failed: {exc}")
        fallback = []
        for job in job_slice:
            if not isinstance(job, dict):
                continue
            title = job.get("titel") or job.get("title") or "Not provided"
            company = job.get("unternehmen") or job.get("company") or "Not provided"
            location = job.get("arbeitsort") or job.get("location") or "Not provided"
            fallback.append({
                "title": title,
                "company": company,
                "location": location,
                "match_score": 0,
                "matching_skills": [],
                "missing_skills": [],
                "recommendation": "Review this role against the applicant profile and language requirements."
            })
        return {"recommendations": fallback}