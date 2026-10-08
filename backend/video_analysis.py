from datetime import datetime

from backend.applicant_state import add_video_analysis


def analyze_video(
    file_path,
    original_filename
):

    result = {
        "filename": original_filename,
        "path": str(file_path),
        "analyzed_at": datetime.utcnow().isoformat(),

        "status": "processed",

        "communication": {
            "clarity": None,
            "confidence": None,
            "structure": None
        },

        "language": {
            "detected": "unknown",
            "level": "not_evaluated"
        },

        "technical": {
            "domain_knowledge": None,
            "explanation_quality": None
        },

        "summary": (
            "Video uploaded successfully. "
            "Advanced speech and visual analysis can be connected "
            "to the agentic verification pipeline."
        ),

        "recommendations": [
            "Evaluate communication clarity.",
            "Evaluate technical explanation.",
            "Evaluate language proficiency.",
            "Compare interview evidence with applicant profile."
        ]
    }

    add_video_analysis(result)

    return result