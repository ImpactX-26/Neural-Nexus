# LearnoryX

## Autonomous Agentic AI for the Germany Applicant Journey

LearnoryX is an AI-powered autonomous applicant journey platform designed for people from India who want to pursue higher education, vocational training, or employment opportunities in Germany.

Instead of functioning as a conventional chatbot, LearnoryX uses an agentic AI architecture to continuously analyze an applicant's profile and documents, identify missing information, evaluate qualification readiness, recommend suitable Germany pathways, generate a personalized roadmap, and determine the applicant's next best action.

The platform is designed as a functional hackathon prototype demonstrating how Agentic AI can simplify and personalize the Germany application journey.

---

## 1. Problem Statement

For applicants from India planning to study, train, or work in Germany, the application journey can be complex and fragmented.

Applicants often need to understand:

* Which Germany pathway is suitable for them
* Whether their academic background is relevant
* Which documents are required
* Whether their documents are complete
* Whether their language proficiency is sufficient
* Which qualifications or skills they are missing
* Which universities, programs, vocational opportunities, or jobs may match their profile
* What they should do next
* How to prepare their CV and application documents
* How to track their overall application readiness

Existing solutions often provide information through static websites, search engines, individual consultants, or simple chatbots.

The applicant is still required to manually connect all the information and decide what to do next.

LearnoryX addresses this problem by introducing an autonomous AI agent that continuously evaluates the applicant's journey and determines the next best action.

---

# 2. Solution

LearnoryX creates a personalized digital applicant journey.

The applicant provides their profile and uploads relevant documents.

The LearnoryX Agent then:

1. Observes the applicant's current state
2. Analyzes profile information
3. Analyzes uploaded documents
4. Extracts relevant information
5. Identifies missing information
6. Evaluates academic qualification
7. Evaluates language readiness
8. Determines suitable Germany pathways
9. Identifies potential opportunities
10. Generates a personalized roadmap
11. Calculates application readiness
12. Selects the highest-priority next action
13. Updates the applicant state
14. Re-evaluates the journey after new information is provided

This creates a continuous:

**Observe → Analyze → Decide → Act → Update → Re-evaluate**

agentic loop.

---

# 3. Vision

Our vision is to create an intelligent digital companion that helps applicants navigate the complete Germany applicant journey with personalized, evidence-based guidance.

LearnoryX aims to transform the traditional:

**Search → Read → Compare → Decide → Apply**

process into:

**Profile → AI Analysis → Autonomous Planning → Personalized Action → Application**

---

# 4. Core Concept

The central concept of LearnoryX is:

> An autonomous applicant journey agent that continuously evaluates applicant state, analyzes available evidence, identifies gaps, determines the next best action, and updates the journey.

The platform combines:

* Applicant profiling
* AI document analysis
* Qualification evaluation
* Language readiness analysis
* Pathway recommendation
* Opportunity matching
* Roadmap generation
* Next-best-action decision making
* CV generation
* Application readiness scoring

---

# 5. Agentic AI Architecture

LearnoryX is designed around an Agent Orchestrator.

The agent receives the applicant's current state and determines what should happen next.

```text
                 APPLICANT
                     |
                     v
            +----------------+
            | Applicant      |
            | Profile        |
            +----------------+
                     |
                     v
            +----------------+
            | Document       |
            | Analysis       |
            +----------------+
                     |
                     v
            +----------------+
            | Qualification  |
            | Evaluation     |
            +----------------+
                     |
                     v
            +----------------+
            | Agent          |
            | Orchestrator   |
            +----------------+
                     |
          +----------+----------+
          |          |          |
          v          v          v
       Analyze    Decide      Act
          |          |          |
          +----------+----------+
                     |
                     v
            +----------------+
            | Applicant State|
            | Update         |
            +----------------+
                     |
                     v
            +----------------+
            | Next Best      |
            | Action         |
            +----------------+
                     |
                     v
             RE-EVALUATION
                     |
                     +-----------> Agent Loop
```

---

# 6. Agentic AI Decision Loop

The core agent loop is:

```text
OBSERVE
   ↓
ANALYZE
   ↓
IDENTIFY GAP
   ↓
DECIDE
   ↓
SELECT TOOL
   ↓
EXECUTE ACTION
   ↓
UPDATE STATE
   ↓
RECALCULATE READINESS
   ↓
SELECT NEXT ACTION
   ↓
RE-EVALUATE
```

For example:

```text
Applicant Profile
       ↓
Missing Transcript Detected
       ↓
Qualification Verification Blocked
       ↓
Agent Identifies Transcript as Priority
       ↓
Next Best Action Generated
       ↓
Applicant Uploads Transcript
       ↓
AI Analyzes Transcript
       ↓
Qualification Updated
       ↓
Readiness Score Updated
       ↓
Agent Selects Next Action
```

This is the primary agentic behavior of LearnoryX.

---

# 7. Key Features

## 7.1 Applicant Profile

Applicants can create a structured profile containing:

### Personal Information

* Full name
* Country
* Email
* Phone

### Education

* Highest qualification
* Degree
* University
* Specialization
* CGPA
* Percentage
* Graduation year

### Skills

* Technical skills
* Programming languages
* AI/ML skills
* Other skills

### Experience

* Fresher / Experienced
* Years of experience
* Job role
* Company

### Languages

* English proficiency
* German proficiency

### Germany Goal

* Higher Education
* Ausbildung
* Employment

### Preferences

* Target field
* Target occupation
* Preferred cities
* Budget

---

# 8. AI-Assisted Document Analysis

Applicants can upload relevant documents.

Supported document categories include:

* Passport
* Degree certificate
* Transcript
* Marks card
* Experience letter
* Language certificate
* CV
* Motivation letter
* Other documents

The system attempts to:

1. Read the document
2. Extract relevant information
3. Classify the document
4. Compare extracted information with the applicant profile
5. Identify missing information
6. Detect potential inconsistencies
7. Update document status

Example output:

```json
{
  "document_type": "Degree Certificate",
  "status": "verified",
  "confidence": 0.94,
  "extracted_information": {
    "degree": "Bachelor of Engineering",
    "specialization": "Artificial Intelligence and Machine Learning",
    "graduation_year": 2026
  },
  "issues": []
}
```

LearnoryX provides AI-assisted document analysis for prototype purposes and does not claim to perform official legal or institutional document verification.

---

# 9. Qualification Analysis

LearnoryX evaluates the applicant's profile against their selected Germany pathway.

The system considers:

* Academic background
* Degree relevance
* Field relevance
* Skills
* Language proficiency
* Experience
* Application preparation
* Available documents

Example:

```text
Qualification Match: 82%

Academic Background: Strong

AI/ML Relevance: High

Language Readiness: Medium

Experience: Needs Improvement

Overall:
Potential match for selected pathways,
subject to institution-specific requirements.
```

The system provides a preliminary assessment and does not guarantee university admission, employment, visa approval, or official eligibility.

---

# 10. Germany Pathway Engine

LearnoryX evaluates three major pathways.

## Higher Education

For applicants interested in:

* Bachelor's programs
* Master's programs
* Related academic programs
* Research-oriented opportunities

## Ausbildung

For applicants interested in:

* Vocational training
* Technical training
* Industry-oriented education
* Practical career pathways

## Employment

For applicants interested in:

* Entry-level opportunities
* Technical roles
* AI/ML roles
* Software roles
* Data-related positions

The agent ranks the pathways based on the applicant's current profile.

Example:

```text
Recommended Pathway

Higher Education
Match Score: 86%

Alternative

Ausbildung
Match Score: 61%

Employment
Match Score: 43%
```

---

# 11. Opportunity Matching

LearnoryX can provide potential opportunities based on the applicant's:

* Education
* Specialization
* Skills
* Language level
* Target pathway
* Location preference

Opportunity categories include:

* Universities
* Master's programs
* Bachelor's programs
* Ausbildung opportunities
* Employment opportunities

Each opportunity can contain:

* Name
* Type
* Field
* Location
* Requirements
* Language requirements
* Match score
* Reason for recommendation
* Application information

For prototype demonstrations, seeded opportunity data may be used.

Applicants should verify current requirements and application information through official sources before applying.

---

# 12. Personalized Roadmap

LearnoryX generates a personalized journey.

Example:

```text
Stage 1
Complete Applicant Profile

Stage 2
Upload Missing Documents

Stage 3
Verify Academic Qualification

Stage 4
Complete Language Requirements

Stage 5
Prepare CV

Stage 6
Prepare Motivation Letter

Stage 7
Shortlist Opportunities

Stage 8
Prepare Applications

Stage 9
Submit Applications

Stage 10
Track Application Status
```

Each stage contains:

* Status
* Priority
* Required action
* Reason
* Expected outcome

Possible statuses:

* Completed
* In Progress
* Pending
* Blocked

---

# 13. Next Best Action Engine

One of the most important LearnoryX features is the Next Best Action Engine.

Instead of giving the applicant a large list of tasks, the agent identifies the highest-priority action.

Example:

```text
NEXT BEST ACTION

Upload your consolidated transcript.

Priority:
HIGH

Why:

Academic qualification verification is currently
blocked because transcript information is missing.

After completion:

The agent will re-evaluate your qualification
and update your recommended opportunities.
```

This allows the system to behave as an autonomous assistant rather than a passive information provider.

---

# 14. Application Readiness Score

LearnoryX calculates an overall readiness score.

The prototype considers:

```text
Profile Completeness       20%
Documents                  20%
Qualification              20%
Language                   15%
Experience                 10%
Application Preparation    15%
```

The final score is normalized to a value between:

```text
0 – 100
```

Example:

```text
Application Readiness

72%
```

The score changes when the applicant completes actions.

For example:

```text
Before Transcript Upload
72%

After Transcript Verification
81%
```

This demonstrates continuous applicant-state updates.

---

# 15. Human-in-the-Loop

LearnoryX separates AI actions from applicant actions.

### AI can:

* Analyze documents
* Extract information
* Identify gaps
* Evaluate qualification
* Recommend pathways
* Generate roadmaps
* Recommend opportunities
* Generate next actions
* Recalculate readiness

### Applicant must:

* Provide information
* Upload documents
* Confirm information
* Correct inaccurate data
* Select final opportunities
* Submit applications
* Make final decisions

This prevents the system from pretending to perform actions that require human authorization.

---

# 16. CV Generator

LearnoryX can generate a professional CV using information from the applicant profile.

CV sections include:

* Name
* Contact information
* Professional summary
* Education
* Skills
* Experience
* Projects
* Certifications
* Languages

The generated CV can be previewed and prepared for printing or download.

---

# 17. Demo Mode

LearnoryX includes a dedicated Demo Mode for hackathons and presentations.

The judge can select:

**Run Full Applicant Analysis**

The system automatically demonstrates:

```text
1. Load applicant
2. Analyze profile
3. Analyze documents
4. Identify missing information
5. Evaluate qualification
6. Evaluate language readiness
7. Recommend Germany pathway
8. Generate opportunities
9. Generate roadmap
10. Calculate readiness
11. Select next best action
```

The UI displays the progress of the agent.

Example:

```text
Analyzing applicant...
DONE

Analyzing documents...
DONE

Evaluating qualification...
DONE

Finding gaps...
DONE

Selecting Germany pathway...
DONE

Generating roadmap...
DONE

Calculating readiness...
DONE

Selecting next action...
DONE
```

---

# 18. Demo Applicant

The prototype includes a sample applicant.

```text
Name:
Ramu Shreeshail Tolamatti

Country:
India

Education:
Engineering

Specialization:
Artificial Intelligence and Machine Learning

English:
B2

German:
A1

Experience:
Fresher

Target:
Germany

Preferred Pathway:
Higher Education
```

Example document state:

```text
Degree Certificate
Verified

Transcript
Missing

Passport
Missing

CV
Available

Language Certificate
Missing
```

This creates an incomplete applicant state that allows the agent to demonstrate autonomous decision-making.

---

# 19. Technology Stack

## Frontend

* React
* Vite
* JavaScript / JSX
* CSS

## Backend

* Python
* FastAPI

## Database

* SQLite
* SQLAlchemy

## AI

* Groq API
* Configurable LLM model
* Structured JSON responses

## Document Processing

* PDF processing
* DOCX processing
* Text extraction
* AI-assisted document analysis

## API Communication

* REST API
* Fetch API

## Development

* VS Code
* Node.js
* Python
* Git

---

# 20. Project Structure

```text
LearnoryX/
│
├── frontend/
│   │
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   ├── App.jsx
│   ├── main.jsx
│   ├── index.css
│   │
│   ├── Navbar.jsx
│   ├── Home.jsx
│   ├── ApplicantJourney.jsx
│   ├── Agent.jsx
│   ├── Profile.jsx
│   ├── Documents.jsx
│   ├── VideoAnalysis.jsx
│   ├── Qualification.jsx
│   ├── CVGenerator.jsx
│   ├── NextSteps.jsx
│   ├── DemoMode.jsx
│   │
│   └── services/
│       └── api.js
│
├── backend/
│   │
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   │
│   ├── agent.py
│   ├── orchestrator.py
│   ├── applicant_state.py
│   ├── profile.py
│   ├── document_service.py
│   ├── document_verification.py
│   ├── qualification.py
│   ├── opportunities.py
│   ├── roadmap.py
│   ├── cv_generator.py
│   ├── ai_service.py
│   ├── demo_data.py
│   └── database.py
│
├── README.md
│
└── .gitignore
```

---

# 21. Backend API

LearnoryX provides the following APIs.

## Health

```http
GET /api/health
```

## Profile

```http
GET /api/profile
POST /api/profile
PUT /api/profile
```

## Documents

```http
GET /api/documents
POST /api/documents/upload
POST /api/documents/analyze
```

## Qualification

```http
GET /api/qualification
POST /api/qualification/analyze
```

## Opportunities

```http
GET /api/opportunities
```

## Agent

```http
POST /api/agent/run
GET /api/agent/status
GET /api/agent/activity
```

## Roadmap

```http
GET /api/roadmap
POST /api/roadmap/generate
```

## Next Action

```http
GET /api/next-action
```

## Demo

```http
POST /api/demo/run
```

## CV

```http
POST /api/cv/generate
```

---

# 22. Installation

## Prerequisites

Install:

* Python 3.10+
* Node.js 18+
* npm
* Git

---

# 23. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 24. Environment Variables

Create:

```text
backend/.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_model_name
DATABASE_URL=sqlite:///./learnoryx.db
```

The frontend should use:

```env
VITE_API_URL=http://localhost:8000
```

Never expose the Groq API key in frontend code.

---

# 25. Running the Backend

From the backend directory:

```bash
uvicorn main:app --reload --port 8000
```

The backend will be available at:

```text
http://localhost:8000
```

FastAPI documentation:

```text
http://localhost:8000/docs
```

---

# 26. Running the Frontend

Open another terminal.

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

# 27. AI Fallback Mode

LearnoryX supports two AI modes.

## Live AI Mode

When a valid Groq API key is configured:

```text
AI MODE: LIVE
```

The application uses the configured LLM.

## Demo AI Mode

If the API is unavailable:

```text
AI MODE: DEMO
```

The system uses deterministic local responses.

This ensures that the prototype remains demonstrable even when:

* API keys are unavailable
* Internet connectivity fails
* API limits are reached
* AI requests fail
* JSON responses are malformed

The application should never completely fail because of an external AI service.

---

# 28. Error Handling

LearnoryX is designed to gracefully handle failures.

Examples:

### Backend unavailable

```text
Backend connection unavailable.
Please start the LearnoryX backend on port 8000.
```

### AI unavailable

```text
Live AI unavailable.
Demo AI mode activated.
```

### Document parsing failure

```text
Document parsing was unsuccessful.
Demo document analysis activated.
```

### Invalid AI JSON

The system attempts:

1. JSON cleanup
2. JSON extraction
3. Retry
4. Demo fallback

The UI should never crash because of malformed AI output.

---

# 29. Agent Tools

The LearnoryX Agent uses internal tools/functions such as:

```text
analyze_profile()

analyze_document()

verify_document()

identify_missing_information()

evaluate_qualification()

evaluate_language_readiness()

recommend_pathway()

search_opportunities()

generate_roadmap()

calculate_readiness()

identify_next_action()

generate_application_checklist()

update_applicant_state()
```

The agent selects the appropriate action based on the current applicant state.

---

# 30. Applicant State

The agent maintains a central applicant state.

Example:

```json
{
  "profile": {},
  "documents": [],
  "qualification": {},
  "language": {},
  "pathway": {},
  "opportunities": [],
  "roadmap": [],
  "missing_items": [],
  "completed_actions": [],
  "next_action": {},
  "readiness_score": 0,
  "agent_status": "analyzing"
}
```

This state is important because the agent does not treat every interaction as an isolated question.

It continuously operates on the applicant's current state.

---

# 31. Example Agent Activity

The dashboard can display:

```text
Agent Activity

12:01
Profile analysis started

12:02
Applicant profile verified

12:03
Document inventory created

12:04
3 required documents missing

12:05
Academic qualification evaluated

12:06
Language readiness evaluated

12:07
Higher Education selected as recommended pathway

12:08
Potential opportunities identified

12:09
Personalized roadmap generated

12:10
Readiness score calculated

12:11
Next best action selected
```

This allows judges to visually understand the autonomous workflow.

---

# 32. Security

The prototype follows basic security principles.

API keys are stored on the backend.

Sensitive configuration is not included in frontend code.

The `.env` file should not be committed.

Example `.gitignore`:

```gitignore
node_modules/
venv/
.env
*.db
__pycache__/
dist/
```

---

# 33. Limitations

LearnoryX is a prototype and should not be considered an official immigration, admission, employment, legal, or visa advisory system.

The system does not guarantee:

* University admission
* Ausbildung acceptance
* Employment
* Visa approval
* Qualification recognition
* Legal eligibility
* Immigration approval

AI-generated recommendations should be independently verified.

Institution-specific requirements may change over time.

Official university, employer, government, and regulatory sources should always be consulted before making final decisions.

---

# 34. Future Scope

Future versions of LearnoryX can include:

## Live University Integration

Connect with university databases and official program APIs.

## Live Opportunity Search

Retrieve current:

* University programs
* Ausbildung opportunities
* Job openings

## Official Document Verification

Integrate with appropriate verification providers.

## Multilingual AI

Support:

* English
* German
* Hindi
* Kannada
* Other Indian languages

## Advanced CV Optimization

Automatically optimize CVs for specific German opportunities.

## Motivation Letter Generation

Generate personalized motivation letters using verified applicant information.

## Application Tracking

Track:

* Applications
* Deadlines
* Responses
* Interviews
* Decisions

## Notification System

Provide:

* Deadline reminders
* Missing-document alerts
* Application updates

## Explainable Recommendations

Show why an opportunity was recommended and which applicant attributes influenced the recommendation.

## Advanced Agent Memory

Maintain long-term applicant journey history.

## Multi-Agent Architecture

Future versions can introduce specialized agents:

```text
Profile Agent
       |
Document Agent
       |
Qualification Agent
       |
Opportunity Agent
       |
Application Agent
       |
Roadmap Agent
       |
Supervisor Agent
```

A supervisor agent could coordinate all specialized agents.

---

# 35. Innovation

The key innovation of LearnoryX is not simply the use of an LLM.

The innovation is the combination of:

```text
Applicant State
+
Evidence Analysis
+
Agentic Decision Making
+
Tool Execution
+
Personalized Planning
+
Next Best Action
+
Continuous Re-evaluation
```

Traditional chatbot:

```text
User Question
      ↓
AI Answer
      ↓
Conversation Ends
```

LearnoryX:

```text
Applicant State
      ↓
AI Observation
      ↓
Evidence Analysis
      ↓
Gap Detection
      ↓
Decision
      ↓
Action
      ↓
State Update
      ↓
Re-evaluation
      ↓
Next Action
      ↓
Continuous Journey
```

This is what makes LearnoryX an Agentic AI application.

---

# 36. Example Use Case

Consider an applicant from India with:

```text
Engineering Degree
AI/ML Specialization
English B2
German A1
No professional experience
```

The applicant uploads their degree certificate.

LearnoryX analyzes the document.

The agent identifies:

```text
Degree:
Verified

Specialization:
AI/ML

Transcript:
Missing

Passport:
Missing

Language Certificate:
Missing
```

The agent then determines:

```text
Qualification:
Potentially suitable

Recommended pathway:
Higher Education

Readiness:
72%

Next action:
Upload transcript
```

After the applicant uploads the transcript:

```text
Document:
Analyzed

Qualification:
Updated

Readiness:
81%

Next action:
Complete language requirement
```

The system continuously updates the applicant journey.

---

# 37. Hackathon Demonstration

The recommended live demonstration is:

### Step 1

Open LearnoryX.

### Step 2

Show the applicant dashboard.

### Step 3

Click:

```text
Run Full Applicant Analysis
```

### Step 4

Show the agent activity.

### Step 5

Show:

```text
Profile Analysis
Document Analysis
Qualification Evaluation
Pathway Recommendation
```

### Step 6

Show the readiness score.

### Step 7

Show missing documents.

### Step 8

Show:

```text
Next Best Action
```

### Step 9

Upload a missing document.

### Step 10

Run the analysis again.

### Step 11

Show the updated applicant state.

### Step 12

Show the updated readiness score.

### Step 13

Show the personalized roadmap.

### Step 14

Show opportunity recommendations.

### Step 15

Show CV generation.

The entire demonstration should take approximately 2–4 minutes.

---

# 38. Why LearnoryX Is Agentic AI

LearnoryX demonstrates agentic AI through five major characteristics.

## 1. State Awareness

The agent knows the applicant's current state.

## 2. Autonomous Decision Making

The agent decides which analysis or action should happen next.

## 3. Tool Usage

The agent can use different functions for:

* Profile analysis
* Document analysis
* Qualification evaluation
* Opportunity matching
* Roadmap generation

## 4. Goal-Oriented Behavior

The agent works toward:

```text
Application Readiness
```

rather than simply answering individual questions.

## 5. Continuous Re-evaluation

When the applicant provides new information, the agent updates the state and determines the next action.

---

# 39. Project Objective

The primary objective of LearnoryX is to demonstrate how Agentic AI can transform a complex, fragmented Germany applicant journey into a personalized, structured, and continuously adaptive experience.

The system aims to reduce:

* Information overload
* Manual planning
* Document confusion
* Qualification uncertainty
* Missed requirements
* Unclear next steps

while improving:

* Personalization
* Applicant awareness
* Decision support
* Journey visibility
* Application preparedness

---

# 40. Project Status

Current prototype capabilities:

* Applicant profile
* Applicant dashboard
* Document management
* AI-assisted document analysis
* Qualification analysis
* Germany pathway recommendation
* Opportunity recommendations
* Personalized roadmap
* Application readiness score
* Next best action
* Agent activity log
* CV generation
* Demo mode
* Live AI mode
* Demo AI fallback
* SQLite persistence
* FastAPI backend
* React frontend

---

# 41. Team

## LearnoryX

Autonomous Agentic AI for the Germany Applicant Journey

Developed as an Agentic AI prototype focused on simplifying the applicant journey from India to Germany.

---

# 42. License

This project is currently intended as a prototype and educational/hackathon project.

License terms can be added according to the project's final ownership and distribution requirements.

---

# 43. Disclaimer

LearnoryX provides AI-assisted recommendations and preliminary assessments.

It is not a replacement for:

* Official university admission offices
* German government authorities
* Immigration professionals
* Credential evaluation organizations
* Employers
* Legal professionals

Applicants must verify all important information through official sources before taking final decisions.

---

# 44. Final Summary

LearnoryX is an autonomous Agentic AI platform designed to simplify the Germany applicant journey.

It transforms fragmented applicant information into a continuously updated journey by combining:

**Profile Analysis**

**Document Intelligence**

**Qualification Assessment**

**Pathway Recommendation**

**Opportunity Matching**

**Personalized Roadmap**

**Next Best Action**

**Application Readiness**

The core intelligence of LearnoryX is its ability to continuously observe applicant state, make decisions, perform actions, update the journey, and determine what should happen next.

The ultimate goal is simple:

> Help every applicant understand where they are, what they are missing, what they should do next, and how they can move closer to their Germany goal.
