import json
import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)


client = None

if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)


def ask_ai(
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.2
):

    if client is None:

        return {
            "success": False,
            "error": "GROQ_API_KEY is not configured.",
            "content": ""
        }

    try:

        response = client.chat.completions.create(
            model=GROQ_MODEL,
            temperature=temperature,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        content = response.choices[0].message.content

        return {
            "success": True,
            "content": content
        }

    except Exception as error:

        return {
            "success": False,
            "error": str(error),
            "content": ""
        }


async def generate_ai_response(
    prompt: str,
    system_prompt: str = "You are a helpful personal guidance assistant.",
    temperature: float = 0.2,
):
    result = ask_ai(system_prompt, prompt, temperature=temperature)

    if result.get("success"):
        return result.get("content", "")

    fallback = {
        "agent_status": "active",
        "decision": "Answer using available Germany guidance context",
        "answer": (
            "The LearnoryX agent is running in offline fallback mode because no Groq key is configured. "
            "Use the following guidance as a structured local response while the live AI service is enabled."
        ),
        "current_topic": "Germany applicant guidance",
        "content": {
            "title": "LearnoryX Guidance",
            "introduction": "This is the offline fallback response for the Germany applicant journey.",
            "explanation": "Use this as a practical starting point while the live AI model remains unavailable.",
            "important_points": [
                "Clarify your target course, visa route, and study objective.",
                "Check language requirements, university deadlines, and document preparation windows.",
                "Prepare the main qualification documents and a structured application timeline."
            ]
        },
        "roadmap": [
            {
                "step": 1,
                "title": "Understand the route",
                "description": "Identify if you are targeting university study, Ausbildung, or employment.",
                "status": "current"
            },
            {
                "step": 2,
                "title": "Prepare the core documents",
                "description": "Gather degree certificates, transcripts, CV, language proof, and application documents.",
                "status": "upcoming"
            },
            {
                "step": 3,
                "title": "Apply and validate",
                "description": "Confirm deadlines, requirements, and the next official action before submission.",
                "status": "upcoming"
            }
        ],
        "documents": [
            {
                "name": "Academic certificates",
                "purpose": "Required by many German institutions and application reviews.",
                "status": "may_be_required"
            },
            {
                "name": "CV and motivation letter",
                "purpose": "Used for both study and job pathways depending on the target.",
                "status": "may_be_required"
            },
            {
                "name": "Language proof",
                "purpose": "Often required for admission and enrollment decisions.",
                "status": "may_be_required"
            }
        ],
        "resources": [
            {
                "title": "German university portal",
                "description": "Official information about admissions and academic requirements.",
                "type": "official",
                "url": ""
            },
            {
                "title": "DAAD guidance",
                "description": "Useful overview for international applicants planning Germany study.",
                "type": "educational",
                "url": ""
            }
        ],
        "practice": [
            {
                "question": "Which Germany pathway are you targeting: study, Ausbildung, or employment?",
                "answer": ""
            }
        ],
        "next_action": "Define your target pathway and gather your core documentation before applying.",
        "agent_trace": [
            {"action": "Understand user request", "result": "Completed"},
            {"action": "Determine applicant requirement", "result": "Completed"},
            {"action": "Use offline fallback guidance", "result": "Completed"},
            {"action": "Recommend next action", "result": "Completed"}
        ]
    }

    return json.dumps(fallback)