import sys
import shutil
import uuid
from pathlib import Path

# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ============================================================
# FASTAPI IMPORTS
# ============================================================

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


# ============================================================
# DATABASE
# ============================================================

from database.database import create_tables


# ============================================================
# LEARNORYX BACKEND MODULES
# ============================================================

from backend.agent import run_agent
from backend.learning_agent import run_learning_agent
from backend.applicant_state import (
    get_applicant_state,
    reset_applicant_state
)
from backend.profile import update_profile
from backend.document_service import process_document
from backend.video_analysis import analyze_video
from backend.qualification import evaluate_qualification
from backend.cv_generator import generate_cv
from backend.next_steps import generate_next_steps
from backend.demo_data import load_demo_applicant
from backend.germany_agent import (
    search_jobs_for_applicant,
    match_jobs_to_applicant,
)


# ============================================================
# DIRECTORIES
# ============================================================

BASE_DIR = PROJECT_ROOT

UPLOAD_DIR = BASE_DIR / "uploads"
DOCUMENT_DIR = UPLOAD_DIR / "documents"
VIDEO_DIR = UPLOAD_DIR / "videos"

DOCUMENT_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# DATABASE TABLES
# ============================================================

create_tables()


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="LearnoryX Agentic AI",
    description=(
        "Agentic AI Applicant Journey Platform for "
        "Study, Ausbildung and Employment in Germany"
    ),
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5175",
        "http://0.0.0.0:5173",
        "http://0.0.0.0:5174",
        "http://0.0.0.0:5175",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# STATIC UPLOADS
# ============================================================

app.mount(
    "/uploads",
    StaticFiles(directory=str(UPLOAD_DIR)),
    name="uploads"
)


# ============================================================
# REQUEST MODELS
# ============================================================

class AgentRequest(BaseModel):
    message: str = ""


class LearningAgentRequest(BaseModel):
    goal: str = ""
    topic: str = ""
    skill_level: str = "Beginner"
    purpose: str = "Germany Study"
    available_time: str = "1 hour/day"
    learning_style: str = "Mixed"


class ProfileRequest(BaseModel):
    name: str = ""
    email: str = ""
    phone: str = ""
    country: str = ""
    education: str = ""
    degree: str = ""
    field: str = ""
    experience: str = ""
    target: str = ""
    german_level: str = ""
    english_level: str = ""


class QualificationRequest(BaseModel):
    target_type: str
    target_name: str
    field: str = ""
    education: str = ""
    experience: str = ""
    german_level: str = ""
    english_level: str = ""


class CVRequest(BaseModel):
    target_role: str
    target_country: str = "Germany"
    language: str = "English"


class GermanyJobRequest(BaseModel):
    keyword: str = "AI Engineer"
    location: str = "Berlin"
    page: int = 1
    size: int = 10


class GermanyApplicantRequest(BaseModel):
    name: str = ""
    email: str = ""
    phone: str = ""
    country: str = "India"
    education: str = ""
    degree: str = ""
    field_of_study: str = ""
    field: str = ""
    skills: list[str] = []
    experience: str = ""
    german_level: str = ""
    english_level: str = ""
    preferred_location: str = "Germany"
    target: str = ""
    target_pathway: str = ""


class AIHealthRequest(BaseModel):
    prompt: str = "Explain artificial intelligence in three sentences."


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "name": "LearnoryX",
        "status": "running",
        "mode": "agentic-ai",
        "version": "1.0.0"
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "agent": "ready",
        "database": "connected",
        "uploads": "ready"
    }


# ============================================================
# APPLICANT STATE
# ============================================================

@app.get("/api/state")
def state():
    return get_applicant_state()


# ============================================================
# AGENT
# ============================================================

@app.post("/api/agent")
def agent(request: AgentRequest):

    message = request.message.strip()

    if not message:
        raise HTTPException(
            status_code=400,
            detail="Agent message cannot be empty."
        )

    try:

        # ----------------------------------------------------
        # RUN AGENT
        # ----------------------------------------------------

        result = run_agent(message)

        if result is None:
            result = {}

        # ----------------------------------------------------
        # CURRENT APPLICANT STATE
        # ----------------------------------------------------

        current_state = result.get(
            "state",
            get_applicant_state()
        )

        # ----------------------------------------------------
        # IMPORTANT:
        # The frontend should display "answer".
        #
        # Different versions of the agent may currently
        # return answer, result or message.
        # This keeps the API compatible with all of them.
        # ----------------------------------------------------

        answer = result.get("answer", "")

        if not answer:
            answer = result.get("response", "")

        if not answer:
            answer = result.get("message", "")

        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        agent_result = result.get("result", "")

        # If result is a dictionary/list, do not force the
        # frontend to render it directly. The agent answer
        # remains the primary human-readable response.
        if not answer and isinstance(agent_result, str):
            answer = agent_result

        # ----------------------------------------------------
        # RETURN COMPLETE AGENT RESPONSE
        # ----------------------------------------------------

        return {
            "success": True,

            "agent_status": result.get(
                "agent_status",
                "completed"
            ),

            "current_stage": result.get(
                "current_stage",
                "analysis"
            ),

            "decision": result.get(
                "decision",
                ""
            ),

            "action": result.get(
                "action",
                ""
            ),

            "answer": answer,

            "result": agent_result,

            "message": result.get(
                "message",
                answer
            ),

            "next_action": result.get(
                "next_action",
                ""
            ),

            "state": current_state,

            "trace": result.get(
                "trace",
                []
            )
        }

    except Exception as error:

        # ----------------------------------------------------
        # AGENT ERROR
        # ----------------------------------------------------

        print(
            "\n=================================================="
        )
        print("LEARNORYX AGENT ERROR")
        print("==================================================")
        print(str(error))
        print(
            "==================================================\n"
        )

        raise HTTPException(
            status_code=500,
            detail=f"Agent execution failed: {str(error)}"
        )


@app.post("/api/learning-agent")
async def learning_agent(request: LearningAgentRequest):
    try:
        result = await run_learning_agent(
            goal=request.goal,
            topic=request.topic,
            skill_level=request.skill_level,
            purpose=request.purpose,
            available_time=request.available_time,
            learning_style=request.learning_style,
        )

        return {
            "success": True,
            "agent_status": result.get("agent_status", "active"),
            "decision": result.get("decision", ""),
            "current_topic": result.get("current_topic", ""),
            "answer": result.get("answer", ""),
            "content": result.get("content", {}),
            "roadmap": result.get("roadmap", []),
            "documents": result.get("documents", []),
            "resources": result.get("resources", []),
            "practice": result.get("practice", []),
            "next_action": result.get("next_action", ""),
            "trace": result.get("agent_trace", []),
            "raw": result,
            "state": get_applicant_state(),
        }
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Learning agent failed: {str(error)}"
        )


# ============================================================
# PROFILE
# ============================================================

@app.post("/api/profile")
def profile(request: ProfileRequest):

    try:

        data = request.model_dump()

        result = update_profile(data)

        return {
            "success": True,
            "profile": result,
            "state": get_applicant_state()
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Profile update failed: {str(error)}"
        )


# ============================================================
# DOCUMENT UPLOAD
# ============================================================

@app.post("/api/documents/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided."
        )

    extension = Path(file.filename).suffix.lower()

    allowed = [
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".png",
        ".jpg",
        ".jpeg"
    ]

    if extension not in allowed:
        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported document format. "
                "Allowed: PDF, DOC, DOCX, TXT, PNG, JPG, JPEG."
            )
        )

    file_id = str(uuid.uuid4())

    safe_name = f"{file_id}{extension}"

    file_path = DOCUMENT_DIR / safe_name

    try:

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        result = process_document(
            file_path=file_path,
            original_filename=file.filename
        )

    except Exception as error:

        if file_path.exists():
            file_path.unlink()

        raise HTTPException(
            status_code=500,
            detail=f"Document processing failed: {str(error)}"
        )

    finally:

        await file.close()

    return {
        "success": True,
        "filename": file.filename,
        "stored_filename": safe_name,
        "file_url": f"/uploads/documents/{safe_name}",
        "result": result,
        "state": get_applicant_state()
    }


# ============================================================
# VIDEO UPLOAD AND ANALYSIS
# ============================================================

@app.post("/api/video/analyze")
async def video(
    file: UploadFile = File(...)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No video filename provided."
        )

    extension = Path(file.filename).suffix.lower()

    allowed = [
        ".mp4",
        ".mov",
        ".avi",
        ".mkv",
        ".webm"
    ]

    if extension not in allowed:
        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported video format. "
                "Allowed: MP4, MOV, AVI, MKV, WEBM."
            )
        )

    file_id = str(uuid.uuid4())

    safe_name = f"{file_id}{extension}"

    file_path = VIDEO_DIR / safe_name

    try:

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        result = analyze_video(
            file_path=file_path,
            original_filename=file.filename
        )

    except Exception as error:

        if file_path.exists():
            file_path.unlink()

        raise HTTPException(
            status_code=500,
            detail=f"Video analysis failed: {str(error)}"
        )

    finally:

        await file.close()

    return {
        "success": True,
        "filename": file.filename,
        "stored_filename": safe_name,
        "file_url": f"/uploads/videos/{safe_name}",
        "result": result,
        "state": get_applicant_state()
    }


# ============================================================
# QUALIFICATION
# ============================================================

@app.post("/api/qualification")
def qualification(
    request: QualificationRequest
):

    try:

        result = evaluate_qualification(
            request.model_dump()
        )

        return {
            "success": True,
            "result": result,
            "state": get_applicant_state()
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=(
                f"Qualification evaluation failed: "
                f"{str(error)}"
            )
        )


# ============================================================
# CV GENERATION
# ============================================================

@app.post("/api/cv")
def cv(
    request: CVRequest
):

    try:

        result = generate_cv(
            request.model_dump()
        )

        return {
            "success": True,
            "result": result,
            "state": get_applicant_state()
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"CV generation failed: {str(error)}"
        )


# ============================================================
# NEXT STEPS
# ============================================================

@app.get("/api/next-steps")
def next_steps():

    try:

        result = generate_next_steps()

        return {
            "success": True,
            "result": result,
            "state": get_applicant_state()
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Next steps generation failed: {str(error)}"
        )


# ============================================================
# GERMANY JOB SEARCH
# ============================================================

@app.post("/api/germany/jobs")
async def germany_jobs(request: GermanyJobRequest):
    try:
        result = await search_germany_jobs(
            keyword=request.keyword,
            location=request.location,
            page=request.page,
            size=request.size,
        )
        return {
            "success": True,
            "source": "Bundesagentur für Arbeit",
            "data": result,
        }
    except Exception as error:
        print(f"[LearnoryX] Germany jobs endpoint failed: {error}")
        raise HTTPException(
            status_code=500,
            detail="Germany jobs service unavailable"
        )


@app.post("/api/germany/applicant")
async def germany_applicant(request: GermanyApplicantRequest):
    try:
        profile = {
            "name": request.name,
            "email": request.email,
            "phone": request.phone,
            "country": request.country,
            "education": request.education,
            "degree": request.degree,
            "field": request.field or request.field_of_study,
            "field_of_study": request.field_of_study or request.field,
            "skills": request.skills,
            "experience": request.experience,
            "german_level": request.german_level,
            "english_level": request.english_level,
            "preferred_location": request.preferred_location or "Germany",
            "target": request.target or request.target_pathway,
            "target_pathway": request.target_pathway or request.target,
        }

        analysis, jobs = await search_jobs_for_applicant(profile)
        matching = await match_jobs_to_applicant(profile, analysis, jobs)

        response = {
            "success": True,
            "agent": "LearnoryX Germany Applicant Agent",
            "profile": profile,
            "result": {
                "analysis": analysis,
                "jobs_found": len(jobs),
                "jobs": jobs,
                "matching": matching,
            },
        }

        return response
    except Exception as exc:
        print(f"[LearnoryX] Germany applicant agent failed: {exc}")
        raise HTTPException(
            status_code=500,
            detail="AI service unavailable"
        )


@app.post("/api/ai/test")
async def ai_test(request: AIHealthRequest):
    try:
        from backend.gemma_service import ask_gemma

        response = await ask_gemma(request.prompt)
        return {
            "success": True,
            "response": response,
        }
    except Exception as error:
        print(f"[LearnoryX] AI test failed: {error}")
        raise HTTPException(
            status_code=500,
            detail="AI service unavailable"
        )


# ============================================================
# DEMO MODE
# ============================================================

@app.post("/api/demo")
def demo():

    try:

        result = load_demo_applicant()

        return {
            "success": True,
            "result": result,
            "state": get_applicant_state()
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Demo mode failed: {str(error)}"
        )


# ============================================================
# RESET
# ============================================================

@app.post("/api/reset")
def reset():

    try:

        reset_applicant_state()

        return {
            "success": True,
            "message": "Applicant state reset.",
            "state": get_applicant_state()
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Applicant reset failed: {str(error)}"
        )