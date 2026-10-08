import { useEffect, useState } from "react";
import {
  ArrowRight,
  Bot,
  CheckCircle2,
  FileText,
  UserRound,
  ShieldCheck
} from "lucide-react";
import { getNextSteps, getState } from "./api";

function NextSteps({ setActivePage }) {
  const [steps, setSteps] = useState([]);
  const [state, setState] = useState(null);

  useEffect(() => {
    const load = async () => {
      const stateResponse = await getState();
      const stepsResponse = await getNextSteps();

      if (stateResponse) setState(stateResponse);
      if (stepsResponse?.result) setSteps(stepsResponse.result);
    };

    load();
  }, []);

  const actions = steps.length ? steps : [
    { action: "Complete applicant profile", reason: "Provide the basic information required to understand your journey.", priority: "Required" },
    { action: "Upload qualification documents", reason: "Provide degrees, certificates or other relevant documents.", priority: "Required" },
    { action: "Verify applicant information", reason: "Review information extracted from your uploaded documents.", priority: "After upload" }
  ];

  return (
    <div className="page">
      <div className="page-header">
        <div>
          <span className="section-label">AGENT RECOMMENDATION</span>
          <h1>Next Steps</h1>
          <p>The agent determines the next useful action from the current applicant state.</p>
        </div>

        <div className="agent-online-large">
          <div className="live-dot"></div>
          Decision ready
        </div>
      </div>

      <section className="next-step-hero">
        <div className="next-agent-icon"><Bot size={25} /></div>
        <div>
          <span>AGENT DECISION</span>
          <h2>{state?.next_action || "Complete your applicant profile first."}</h2>
          <p>{state?.agent?.reasoning_summary || "LearnoryX needs basic applicant information before it can reliably evaluate documents and qualification pathways."}</p>
        </div>
      </section>

      <section className="next-actions">
        {actions.map((action, index) => {
          const fallbackIcon = index % 3 === 0 ? UserRound : index % 3 === 1 ? FileText : ShieldCheck;
          const Icon = fallbackIcon;

          return (
            <div className="next-action-card" key={`${action.action}-${index}`}>
              <div className="next-action-number">{String(index + 1).padStart(2, "0")}</div>
              <div className="next-action-icon"><Icon size={19} /></div>
              <div className="next-action-content">
                <div className="next-action-title">
                  <h3>{action.action || action.title}</h3>
                  <span>{action.priority || "Suggested"}</span>
                </div>
                <p>{action.reason || action.description}</p>
              </div>

              <button className="icon-button" onClick={() => setActivePage(action.action === "Complete applicant profile" ? "profile" : action.action.includes("document") ? "documents" : "journey")}>
                <ArrowRight size={17} />
              </button>
            </div>
          );
        })}
      </section>

      <div className="agent-note">
        <CheckCircle2 size={20} />
        <div>
          <strong>Why this action?</strong>
          <p>The agent selects actions according to missing information, verification status, completed tasks and the applicant's current objective.</p>
        </div>
      </div>
    </div>
  );
}

export default NextSteps;