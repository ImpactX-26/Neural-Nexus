import json
import re

from backend.ai_service import generate_ai_response


def clean_text(value):
    if value is None:
        return ""

    text = str(value)

    # Remove markdown and decorative symbols
    text = re.sub(r"[*_`#~]", "", text)

    # Remove bullets and decorative characters
    text = re.sub(r"[•●▪◦◆◇▶►✓✔✦✧★☆→←↑↓]", "", text)

    # Keep normal punctuation useful for readable sentences
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def clean_data(value):
    if isinstance(value, dict):
        return {
            key: clean_data(val)
            for key, val in value.items()
        }

    if isinstance(value, list):
        return [
            clean_data(item)
            for item in value
        ]

    if isinstance(value, str):
        return clean_text(value)

    return value


async def run_learning_agent(
    goal: str,
    topic: str = "",
    skill_level: str = "Beginner",
    purpose: str = "Germany Study",
    available_time: str = "1 hour/day",
    learning_style: str = "Mixed",
):
    user_question = goal.strip()

    prompt = f"""
You are LearnoryX Germany Applicant Agent.

You are an autonomous AI agent helping applicants from India understand and plan their journey to Germany.

The user can ask ANY question.

The question may be about:

Germany study

German universities

Bachelor programs

Master programs

Vocational training

Ausbildung

Jobs in Germany

German language

Student applications

University applications

Admission requirements

Documents

Degree certificates

Marksheets

Transcripts

Experience letters

CV

Motivation letters

Qualification evaluation

Document verification

Visa preparation

Blocked account

Health insurance

Accommodation

APS related topics

Language requirements

Application planning

Career pathways

Learning German

Financial planning

Application timelines

Or any other Germany related topic.

Do not behave like a simple chatbot.

You are an agent.

You must analyze the user question.

Determine what the applicant needs.

Determine what information is missing.

Create the appropriate roadmap.

Provide useful content.

Identify required documents when relevant.

Recommend the next action.

Adapt the response to the applicant's goal.

If the question is unrelated to Germany, answer the question normally while remaining useful.

USER GOAL

{goal}

TOPIC

{topic}

SKILL LEVEL

{skill_level}

PURPOSE

{purpose}

AVAILABLE TIME

{available_time}

LEARNING STYLE

{learning_style}

IMPORTANT BEHAVIOR

If the user asks a direct question, answer that question directly.

Do not force every question into a learning course.

If the user asks about Germany, provide Germany specific content.

If documents are relevant, explain which documents are normally needed and why.

Do not claim that a document is legally mandatory unless you are certain.

Use wording such as commonly required, may be required, or depends on the institution when appropriate.

If the user asks about study, explain the relevant study pathway.

If the user asks about Ausbildung, explain the vocational pathway.

If the user asks about employment, explain the employment pathway.

If the user asks about German language, provide a practical language roadmap.

If the user asks about documents, explain document preparation and verification.

If the user asks about visa related matters, clearly distinguish general preparation information from official immigration decisions.

Never invent personal information.

Never invent a university.

Never invent a company.

Never invent a qualification.

Never invent a document.

Never invent a URL.

Do not return markdown.

Do not use emojis.

Do not use decorative symbols.

Do not use bullet symbols.

Use plain professional text.

Return ONLY valid JSON.

JSON FORMAT

{{
    "agent_status": "active",
    "decision": "Explain the decision made by the agent",

    "answer": "Direct answer to the user's question",

    "current_topic": "The topic currently being handled",

    "content": {{
        "title": "Content title",
        "introduction": "Short introduction",
        "explanation": "Detailed explanation",
        "important_points": [
            "Point one",
            "Point two",
            "Point three"
        ]
    }},

    "roadmap": [
        {{
            "step": 1,
            "title": "First step",
            "description": "Description",
            "status": "current"
        }},
        {{
            "step": 2,
            "title": "Second step",
            "description": "Description",
            "status": "upcoming"
        }},
        {{
            "step": 3,
            "title": "Third step",
            "description": "Description",
            "status": "upcoming"
        }}
    ],

    "documents": [
        {{
            "name": "Document name",
            "purpose": "Why it may be needed",
            "status": "required_or_may_be_required_or_not_required"
        }}
    ],

    "resources": [
        {{
            "title": "Resource title",
            "description": "Resource description",
            "type": "official_or_educational",
            "url": ""
        }}
    ],

    "practice": [
        {{
            "question": "Question for the applicant",
            "answer": ""
        }}
    ],

    "next_action": "The single most useful next action for the applicant",

    "agent_trace": [
        {{
            "action": "Understand user request",
            "result": "Completed"
        }},
        {{
            "action": "Determine applicant requirement",
            "result": "Completed"
        }},
        {{
            "action": "Select relevant information",
            "result": "Completed"
        }},
        {{
            "action": "Determine next action",
            "result": "Completed"
        }}
    ]
}}

IMPORTANT

Answer the actual user question.

Do not generate generic content when the user asks a specific question.

For example, if the user asks:

What documents do I need for Germany study

Answer specifically about documents.

If the user asks:

What is Ausbildung

Answer specifically about Ausbildung.

If the user asks:

How can I learn German

Create a German learning roadmap.

If the user asks:

Can I study computer science in Germany

Explain the pathway and information the applicant should check.

If the user asks:

What should I do next

Use the available context and determine the next logical applicant action.

If the user asks something outside Germany, answer it normally.

All displayed text must be plain professional text without decorative symbols.
"""

    try:
        raw = await generate_ai_response(prompt)

        if isinstance(raw, dict):
            result = raw
        else:
            result = json.loads(raw)

        result = clean_data(result)

        if "answer" not in result:
            result["answer"] = (
                "The agent could not generate a direct answer."
            )

        if "roadmap" not in result:
            result["roadmap"] = []

        if "content" not in result:
            result["content"] = {
                "title": "",
                "introduction": "",
                "explanation": "",
                "important_points": []
            }

        if "documents" not in result:
            result["documents"] = []

        if "resources" not in result:
            result["resources"] = []

        if "practice" not in result:
            result["practice"] = []

        if "next_action" not in result:
            result["next_action"] = (
                "Review the information and continue with the next applicant step."
            )

        if "agent_trace" not in result:
            result["agent_trace"] = []

        return result

    except json.JSONDecodeError:
        return {
            "agent_status": "active",
            "decision": "Generate a direct response",
            "answer": clean_text(raw),
            "current_topic": topic or goal,
            "content": {
                "title": "LearnoryX Agent Response",
                "introduction": "",
                "explanation": clean_text(raw),
                "important_points": []
            },
            "roadmap": [],
            "documents": [],
            "resources": [],
            "practice": [],
            "next_action": "Ask the agent your next question.",
            "agent_trace": [
                {
                    "action": "Understand user request",
                    "result": "Completed"
                },
                {
                    "action": "Generate response",
                    "result": "Completed"
                }
            ]
        }

    except Exception as error:
        return {
            "agent_status": "error",
            "decision": "Agent execution failed",
            "answer": (
                "The LearnoryX agent could not process the request. "
                "Please try the question again."
            ),
            "current_topic": topic or goal,
            "content": {
                "title": "Agent Response",
                "introduction": "",
                "explanation": "",
                "important_points": []
            },
            "roadmap": [],
            "documents": [],
            "resources": [],
            "practice": [],
            "next_action": "Try the request again.",
            "agent_trace": [
                {
                    "action": "Agent execution",
                    "result": "Failed"
                }
            ]
        }