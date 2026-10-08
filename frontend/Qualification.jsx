import { useEffect, useState } from "react";
import {
  GraduationCap,
  BriefcaseBusiness,
  Target,
  CheckCircle2,
  AlertCircle
} from "lucide-react";
import { evaluateQualification, getState } from "./api";

function Qualification() {
  const [state, setState] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadState = async () => {
      const response = await getState();
      if (response) setState(response);
    };
    loadState();
  }, []);

  const runQualification = async () => {
    setLoading(true);
    setError("");

    const applicant = state?.applicant || {};
    const payload = {
      target_type: applicant.target || "study",
      target_name: applicant.target || "Study",
      field: applicant.field || "",
      education: applicant.education || "",
      experience: applicant.experience || "",
      german_level: applicant.german_level || "",
      english_level: applicant.english_level || ""
    };

    const response = await evaluateQualification(payload);
    setLoading(false);

    if (!response.success) {
      setError(response.error || "Qualification analysis failed.");
      return;
    }

    const refreshed = await getState();
    setState(refreshed);
  };

  const qualification = state?.qualification || {};
  const applicant = state?.applicant || {};

  const pathways = [
    { title: "Study", icon: GraduationCap, status: qualification.pathway === "Study" ? "Ready" : "Pending", description: "Academic pathway analysis based on verified education information." },
    { title: "Vocational Training", icon: Target, status: qualification.pathway === "Vocational Training" ? "Ready" : "Pending", description: "Training pathway analysis based on qualification and applicant goals." },
    { title: "Employment", icon: BriefcaseBusiness, status: qualification.pathway === "Employment" ? "Ready" : "Pending", description: "Employment pathway analysis based on skills and professional experience." }
  ];

  return (
    <div className="page">
      <div className="page-header">
        <div>
          <span className="section-label">QUALIFICATION ENGINE</span>
          <h1>Qualification Analysis</h1>
          <p>Compare verified applicant information with relevant pathways.</p>
        </div>

        <button className="primary-button" onClick={runQualification} disabled={loading}>
          {loading ? "Evaluating..." : "Run Qualification"}
        </button>
      </div>

      <section className="qualification-summary">
        <div>
          <span>Applicant qualification state</span>
          <strong>{qualification.status || "not_evaluated"}</strong>
        </div>

        <div>
          <span>Analysis readiness</span>
          <strong>{qualification.status === "not_evaluated" ? "Not ready" : "Ready"}</strong>
        </div>

        <div>
          <span>Verified information</span>
          <strong>{applicant.name ? "Available" : "Pending"}</strong>
        </div>
      </section>

      {error && <div className="error-box">{error}</div>}

      <div className="section-heading compact">
        <div>
          <span className="section-label">PATHWAYS</span>
          <h2>Potential directions</h2>
        </div>
      </div>

      <section className="pathway-analysis-grid">
        {pathways.map((pathway) => {
          const Icon = pathway.icon;
          return (
            <div className="qualification-card" key={pathway.title}>
              <div className="qualification-icon"><Icon size={22} /></div>
              <div className="qualification-card-header">
                <h3>{pathway.title}</h3>
                <span className="status-pill warning"><AlertCircle size={13} />{pathway.status}</span>
              </div>
              <p>{pathway.description}</p>
              <div className="qualification-requirement"><CheckCircle2 size={15} /><span>{qualification.matches?.length ? "Verified requirements available" : "Verified applicant data required"}</span></div>
            </div>
          );
        })}
      </section>

      {qualification && Object.keys(qualification).length > 0 && (
        <section className="agent-note">
          <GraduationCap size={20} />
          <div>
            <strong>Qualification details</strong>
            <p>{qualification.explanation || "No explanation available yet."}</p>
            <pre>{JSON.stringify(qualification, null, 2)}</pre>
          </div>
        </section>
      )}
    </div>
  );
}

export default Qualification;