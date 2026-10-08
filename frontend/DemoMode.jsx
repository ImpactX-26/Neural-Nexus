import { useState } from "react";
import {
  PlayCircle,
  Bot,
  UserRound,
  FileText,
  GraduationCap,
  ArrowRight
} from "lucide-react";
import { loadDemo, resetApplicant } from "./api";

function DemoMode({ setActivePage }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleLoadDemo = async () => {
    setLoading(true);
    setError("");
    const response = await loadDemo();
    setLoading(false);

    if (!response.success) {
      setError(response.error || "Demo could not be loaded.");
      return;
    }

    setActivePage("journey");
  };

  const handleReset = async () => {
    setLoading(true);
    setError("");
    const response = await resetApplicant();
    setLoading(false);

    if (!response.success) {
      setError(response.error || "Reset failed.");
    }
  };

  const demoSteps = [
    { number: "01", title: "Applicant enters Germany goal", icon: UserRound },
    { number: "02", title: "Agent collects applicant profile", icon: Bot },
    { number: "03", title: "Applicant uploads documents", icon: FileText },
    { number: "04", title: "Agent extracts and verifies information", icon: Bot },
    { number: "05", title: "Qualification pathways are analyzed", icon: GraduationCap },
    { number: "06", title: "Agent determines next action", icon: ArrowRight }
  ];

  return (
    <div className="page">
      <div className="page-header">
        <div>
          <span className="section-label">DEMO MODE</span>
          <h1>Experience LearnoryX</h1>
          <p>Follow a simulated applicant journey to understand how the agentic workflow operates.</p>
        </div>

        <div className="hero-actions">
          <button className="primary-button" onClick={handleLoadDemo} disabled={loading}>
            <PlayCircle size={17} />
            {loading ? "Loading..." : "Start Demo"}
          </button>
          <button className="secondary-button" onClick={handleReset} disabled={loading}>Reset</button>
        </div>
      </div>

      {error && <div className="error-box">{error}</div>}

      <section className="demo-hero">
        <div className="demo-icon"><Bot size={28} /></div>
        <h2>Agentic applicant journey</h2>
        <p>This demo shows how LearnoryX can move from applicant input to structured information, verification, qualification and next-step decisions.</p>
      </section>

      <section className="demo-timeline">
        {demoSteps.map((step, index) => {
          const Icon = step.icon;
          return (
            <div className="demo-step" key={step.number}>
              <div className="demo-step-number">{step.number}</div>
              <div className="demo-step-icon"><Icon size={19} /></div>
              <div>
                <span>STAGE {index + 1}</span>
                <h3>{step.title}</h3>
              </div>
              {index < demoSteps.length - 1 && <div className="demo-connector"></div>}
            </div>
          );
        })}
      </section>
    </div>
  );
}

export default DemoMode;