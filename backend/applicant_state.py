from datetime import datetime
from copy import deepcopy


_DEFAULT_STATE = {
    "applicant": {
        "name": "",
        "email": "",
        "phone": "",
        "country": "India",
        "education": "",
        "degree": "",
        "field": "",
        "experience": "",
        "target": "",
        "german_level": "",
        "english_level": ""
    },
    "applicant_profile": {
        "name": "",
        "email": "",
        "phone": "",
        "country": "India",
        "education": "",
        "degree": "",
        "field": "",
        "experience": "",
        "target": "",
        "german_level": "",
        "english_level": ""
    },
    "education": {
        "highest_education": "",
        "degree": "",
        "field": ""
    },
    "experience": {
        "summary": ""
    },
    "documents": [],
    "document_verification": [],
    "video_analysis": [],
    "language": {
        "german_level": "",
        "english_level": ""
    },
    "target_pathway": "",
    "qualification": {
        "status": "not_evaluated",
        "matches": [],
        "gaps": [],
        "recommendations": [],
        "pathway": "",
        "confidence": 0,
        "explanation": ""
    },
    "cv": {
        "generated": False,
        "content": ""
    },
    "next_steps": [],
    "journey_progress": {
        "current_stage": "profile",
        "completed": [],
        "pending": [
            "profile",
            "documents",
            "verification",
            "video",
            "qualification",
            "cv",
            "next_steps"
        ],
        "blocked": [],
        "progress_percent": 0
    },
    "missing_information": [],
    "missing_documents": [],
    "completed_actions": [],
    "pending_actions": [],
    "blocked_actions": [],
    "agent_history": [],
    "last_action": "",
    "next_action": "collect_profile",
    "agent_status": "idle",
    "current_stage": "profile",
    "decision": "",
    "agent": {
        "current_goal": "",
        "current_action": "",
        "last_action": "",
        "last_result": "",
        "reasoning_summary": "",
        "completed_actions": [],
        "pending_actions": [],
        "status": "idle"
    },
    "metadata": {
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }
}


_state = deepcopy(_DEFAULT_STATE)


def _normalize_state(state):
    state = deepcopy(state)
    applicant = state.get("applicant") or {}
    applicant_profile = state.get("applicant_profile") or applicant.copy()
    state["applicant_profile"] = applicant_profile
    state["applicant"] = applicant

    if not state.get("language"):
        state["language"] = {
            "german_level": applicant.get("german_level", ""),
            "english_level": applicant.get("english_level", "")
        }

    state["target_pathway"] = state.get("target_pathway") or applicant.get("target", "")
    state["current_stage"] = state.get("current_stage") or state.get("journey_progress", {}).get("current_stage", "profile")
    state["agent_status"] = state.get("agent_status") or state.get("agent", {}).get("status", "idle")
    state["agent_history"] = state.get("agent_history", [])
    state["completed_actions"] = state.get("completed_actions", [])
    state["pending_actions"] = state.get("pending_actions", [])
    state["blocked_actions"] = state.get("blocked_actions", [])
    state["missing_information"] = state.get("missing_information", [])
    state["missing_documents"] = state.get("missing_documents", [])
    state["next_action"] = state.get("next_action") or "collect_profile"
    state["decision"] = state.get("decision", "")
    return state


def get_applicant_state():
    return deepcopy(_normalize_state(_state))


def update_state(section, data):
    global _state

    _state = _normalize_state(_state)

    if section == "applicant":
        _state["applicant"] = deepcopy(data)
        _state["applicant_profile"] = deepcopy(data)
        _state["language"]["german_level"] = data.get("german_level", _state["language"].get("german_level", ""))
        _state["language"]["english_level"] = data.get("english_level", _state["language"].get("english_level", ""))
        _state["target_pathway"] = data.get("target", _state.get("target_pathway", ""))
    elif section == "agent":
        _state["agent"] = {**_state.get("agent", {}), **data}
        _state["agent_status"] = _state["agent"].get("status", _state["agent_status"])
    else:
        if section not in _state:
            _state[section] = {}
        if isinstance(_state[section], dict):
            _state[section].update(data)
        else:
            _state[section] = data

    _state["metadata"]["updated_at"] = datetime.utcnow().isoformat()
    return get_applicant_state()


def set_state(new_state):
    global _state
    _state = _normalize_state(new_state)
    _state["metadata"]["updated_at"] = datetime.utcnow().isoformat()
    return get_applicant_state()


def reset_applicant_state():
    global _state

    _state = deepcopy(_DEFAULT_STATE)
    _state["metadata"]["updated_at"] = datetime.utcnow().isoformat()
    return get_applicant_state()


def add_document(document):
    global _state

    _state = _normalize_state(_state)
    _state["documents"].append(document)
    _state["document_verification"].append({
        "filename": document.get("filename", ""),
        "status": document.get("verification", {}).get("status", "pending"),
        "confidence": document.get("verification", {}).get("confidence", 0)
    })
    _state["metadata"]["updated_at"] = datetime.utcnow().isoformat()
    return get_applicant_state()


def add_video_analysis(result):
    global _state

    _state = _normalize_state(_state)
    _state["video_analysis"].append(result)
    _state["metadata"]["updated_at"] = datetime.utcnow().isoformat()
    return get_applicant_state()


def add_completed_action(action):
    global _state

    _state = _normalize_state(_state)
    completed = _state["agent"].get("completed_actions", [])
    if action not in completed:
        completed.append(action)
    _state["agent"]["completed_actions"] = completed
    _state["agent"]["last_action"] = action
    _state["completed_actions"] = completed
    _state["metadata"]["updated_at"] = datetime.utcnow().isoformat()
    return get_applicant_state()


def set_agent_status(
    status,
    current_action="",
    reasoning_summary="",
    last_result=""
):
    global _state

    _state = _normalize_state(_state)
    _state["agent_status"] = status
    _state["current_stage"] = _state.get("journey_progress", {}).get("current_stage", "profile")
    _state["agent"]["status"] = status
    _state["agent"]["current_action"] = current_action
    _state["agent"]["reasoning_summary"] = reasoning_summary
    _state["agent"]["last_result"] = last_result
    _state["last_action"] = current_action or _state.get("last_action", "")
    _state["next_action"] = current_action or _state.get("next_action", "collect_profile")

    _state["metadata"]["updated_at"] = datetime.utcnow().isoformat()
    return get_applicant_state()