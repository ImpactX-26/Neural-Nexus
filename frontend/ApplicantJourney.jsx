import { useEffect, useState } from "react";
import {
  CheckCircle2,
  Circle,
  FileText,
  GraduationCap,
  UserRound,
  Video,
  FileUser,
  ArrowRight
} from "lucide-react";
import { getState } from "./api";

function ApplicantJourney({ setActivePage }) {
  const [state, setState] = useState(null);

  useEffect(() => {
    const loadState = async () => {
      const response = await getState();
      if (response && response.applicant) setState(response);
    };
    loadState();
  }, []);

  const applicant = state?.applicant || {};
  const progress = state?.journey_progress || {};
  const currentStage = state?.current_stage || "profile";

  const stages = [
    { id: 1, title: "Profile", description: "Basic identity, education, experience and goals.", icon: UserRound, page: "profile" },
    { id: 2, title: "Documents", description: "Upload and process relevant applicant documents.", icon: FileText, page: "documents" },
    { id: 3, title: "Verification", description: "Validate extracted information and identify inconsistencies.", icon: CheckCircle2, page: "documents" },
    { id: 4, title: "Video / Interview", description: "Analyze applicant responses and video evidence.", icon: Video, page: "video" },
    { id: 5, title: "Qualification", description: "Evaluate education and experience against pathways.", icon: GraduationCap, page: "qualification" },
    { id: 6, title: "CV", description: "Generate a structured CV using verified information.", icon: FileUser, page: "cv" },
    { id: 7, title: "Next Steps", description: "The agent determines the next action for the applicant.", icon: ArrowRight, page: "next" }
  ];

  const stageStatus = (stagePage) => {
    if (currentStage === stagePage) return "active";
    if (progress.completed?.includes(stagePage)) return "completed";
    if (progress.blocked?.includes(stagePage)) return "blocked";
    return "pending";
  };

  return (
    <div className="page">
      <div className="page-header">
        <div>
          <span className="section-label">APPLICANT JOURNEY</span>
          <h1>Journey orchestration</h1>
          <p>LearnoryX dynamically manages the applicant journey instead of following a fixed sequence.</p>
        </div>

        <div className="journey-status">
          <span>Overall progress</span>
          <strong>{progress.progress_percent || 0}%</strong>
        </div>
      </div>

      <div className="journey-layout">
        <section className="journey-timeline">
          {stages.map((stage, index) => {
            const Icon = stage.icon;
            const status = stageStatus(stage.page);

            return (
              <div className="timeline-item" key={stage.id}>
                <div className="timeline-marker">
                  {status === "active" ? <Icon size={18} /> : <Circle size={17} />}
                </div>

                {index !== stages.length - 1 && <div className="timeline-line"></div>}

                <div className="timeline-content">
                  <div>
                    <span className="stage-number">STEP {String(stage.id).padStart(2, "0")}</span>
                    <h3>{stage.title}</h3>
                    <p>{stage.description}</p>
                  </div>

                  <button className="small-button" onClick={() => setActivePage(stage.page)}>
                    Open
                    <ArrowRight size={14} />
                  </button>
                </div>
              </div>
            );
          })}
        </section>

        <aside className="journey-agent-card">
          <div className="card-icon"><CheckCircle2 size={21} /></div>
          <span className="section-label">AGENT DECISION</span>
          <h3>{state?.next_action || "collect_profile"}</h3>
          <p>The agent checks the current applicant state before selecting the next action.</p>

          <div className="agent-reasoning">
            <div>
              <span>Current state</span>
              <strong>{applicant.name || "Applicant profile pending"}</strong>
            </div>
            <div>
              <span>Missing data</span>
              <strong>{state?.missing_information?.length ? state.missing_information.join(", ") : "None detected"}</strong>
            </div>
            <div>
              <span>Selected action</span>
              <strong>{state?.next_action || "collect_profile"}</strong>
            </div>
          </div>

          <button className="primary-button full-width" onClick={() => setActivePage("profile")}>
            Continue Journey
            <ArrowRight size={16} />
          </button>
        </aside>
      </div>
    </div>
  );
}

export default ApplicantJourney;