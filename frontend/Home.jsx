import { useEffect, useState } from "react";
import {
  ArrowRight,
  Bot,
  FileCheck2,
  GraduationCap,
  ShieldCheck,
  Sparkles,
  UserRound,
  RefreshCw
} from "lucide-react";
import { checkBackend, getState, loadDemo, resetApplicant } from "./api";

function Home({ setActivePage }) {
  const [state, setState] = useState(null);
  const [backendStatus, setBackendStatus] = useState("checking");
  const [loading, setLoading] = useState(false);

  const refreshState = async () => {
    const backendResponse = await checkBackend();
    if (backendResponse?.status === "healthy") {
      setBackendStatus("healthy");
    } else {
      setBackendStatus("offline");
    }

    const stateResponse = await getState();
    if (stateResponse && stateResponse.applicant) {
      setState(stateResponse);
    }
  };

  useEffect(() => {
    refreshState();
  }, []);

  const applicant = state?.applicant || {};
  const nextAction = state?.next_action || state?.agent?.current_action || "collect_profile";
  const progressPercent = state?.journey_progress?.progress_percent || 0;

  const handleLoadDemo = async () => {
    setLoading(true);
    const response = await loadDemo();
    setLoading(false);
    if (response?.success) {
      setState(response.state);
      setActivePage("journey");
    }
  };

  const handleReset = async () => {
    setLoading(true);
    const response = await resetApplicant();
    setLoading(false);
    if (response?.success) {
      setState(response.state);
    }
  };

  const features = [
    {
      icon: UserRound,
      title: "Progressive Applicant Profile",
      text: "LearnoryX continuously builds your applicant profile as new information becomes available."
    },
    {
      icon: FileCheck2,
      title: "Document Intelligence",
      text: "Extract and analyze information from degrees, certificates and experience documents."
    },
    {
      icon: GraduationCap,
      title: "Qualification Analysis",
      text: "Understand how your education and experience relate to potential pathways."
    },
    {
      icon: ShieldCheck,
      title: "Verification Layer",
      text: "Important information is checked before the agent uses it for decisions."
    }
  ];

  return (
    <div className="page">
      <section className="hero">
        <div className="hero-content">
          <div className="eyebrow">
            <Sparkles size={15} />
            Agentic AI Applicant Journey
          </div>

          <h1>
            Your intelligent journey
            <span> to Germany.</span>
          </h1>

          <p className="hero-description">
            LearnoryX understands your profile, analyzes your documents,
            evaluates your qualifications and continuously decides what
            should happen next in your applicant journey.
          </p>

          <div className="hero-actions">
            <button className="primary-button" onClick={() => setActivePage("journey")}>
              Start Applicant Journey
              <ArrowRight size={17} />
            </button>

            <button className="secondary-button" onClick={() => setActivePage("agent")}>
              <Bot size={17} />
              Open AI Agent
            </button>
          </div>

          <div className="hero-actions">
            <button className="secondary-button" onClick={handleLoadDemo} disabled={loading}>
              Load Demo
            </button>
            <button className="secondary-button" onClick={handleReset} disabled={loading}>
              <RefreshCw size={16} />
              Reset
            </button>
          </div>
        </div>

        <div className="agent-preview">
          <div className="preview-header">
            <div>
              <span>LEARNORYX AGENT</span>
              <h3>Current Decision</h3>
            </div>
            <div className="live-dot"></div>
          </div>

          <div className="decision-box">
            <div className="decision-icon">
              <Bot size={21} />
            </div>
            <div>
              <strong>{nextAction || "Collect profile information"}</strong>
              <p>
                {state ? `Current status: ${state.agent_status || "idle"}` : "Backend status is being checked."}
              </p>
            </div>
          </div>

          <div className="agent-flow">
            <div className="flow-step completed"><span>1</span><p>Observe</p></div>
            <div className="flow-line"></div>
            <div className="flow-step active"><span>2</span><p>Decide</p></div>
            <div className="flow-line"></div>
            <div className="flow-step"><span>3</span><p>Execute</p></div>
            <div className="flow-line"></div>
            <div className="flow-step"><span>4</span><p>Verify</p></div>
          </div>
        </div>
      </section>

      <section className="section-heading">
        <div>
          <span className="section-label">SYSTEM STATUS</span>
          <h2>Applicant overview</h2>
        </div>
        <p>
          Backend: <strong>{backendStatus}</strong> • Applicant: <strong>{applicant.name || "Not started"}</strong>
        </p>
      </section>

      <section className="feature-grid">
        <div className="feature-card">
          <div className="feature-icon"><Bot size={20} /></div>
          <h3>Agent Status</h3>
          <p>{state?.agent_status || "idle"}</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon"><UserRound size={20} /></div>
          <h3>Current Journey Stage</h3>
          <p>{state?.current_stage || "profile"}</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon"><ShieldCheck size={20} /></div>
          <h3>Progress</h3>
          <p>{progressPercent}%</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon"><FileCheck2 size={20} /></div>
          <h3>Recommended Next Action</h3>
          <p>{nextAction}</p>
        </div>
      </section>

      <section className="pathway-section">
        <div>
          <span className="section-label">SUPPORTED PATHWAYS</span>
          <h2>Study, vocational training or employment.</h2>
          <p>
            LearnoryX structures the applicant journey around the pathway that best matches the information available in the applicant state.
          </p>
        </div>
        <div className="pathway-cards">
          <div className="pathway-card"><GraduationCap size={20} /><strong>Study</strong><span>Higher education pathways</span></div>
          <div className="pathway-card"><FileCheck2 size={20} /><strong>Vocational Training</strong><span>Training and qualification pathways</span></div>
          <div className="pathway-card"><UserRound size={20} /><strong>Employment</strong><span>Career and employment pathways</span></div>
        </div>
      </section>
    </div>
  );
}

export default Home;