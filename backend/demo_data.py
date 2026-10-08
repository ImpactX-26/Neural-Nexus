from backend.applicant_state import set_state
from datetime import datetime


def load_demo_applicant():

    demo = {
        "applicant": {
            "name": "Demo Applicant",
            "email": "demo@example.com",
            "phone": "+91 9000000000",
            "country": "India",
            "education": "Bachelor's Degree",
            "degree": "Bachelor of Engineering",
            "field": "Artificial Intelligence and Machine Learning",
            "experience": "Academic projects and software development",
            "target": "AI Engineer",
            "german_level": "A2",
            "english_level": "B2"
        },

        "documents": [],

        "video_analysis": [],

        "qualification": {
            "status": "not_evaluated",
            "matches": [],
            "gaps": [],
            "recommendations": []
        },

        "cv": {
            "generated": False,
            "content": ""
        },

        "next_steps": [],

        "agent": {
            "current_goal": "Germany AI career pathway",
            "current_action": "",
            "last_action": "",
            "last_result": "",
            "reasoning_summary": "",
            "completed_actions": [],
            "pending_actions": [],
            "status": "demo_loaded"
        },

        "metadata": {
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
            "mode": "demo"
        }
    }

    return set_state(demo)