import { useEffect, useState } from "react";
import {
  FileUser,
  Sparkles,
  Download,
  CheckCircle2
} from "lucide-react";
import { generateCV, getState } from "./api";

function CVGenerator() {
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

  const handleGenerateCV = async () => {
    setLoading(true);
    setError("");

    const applicant = state?.applicant || {};
    const payload = {
      target_role: applicant.target || "AI Engineer",
      target_country: "Germany",
      language: "English"
    };

    const response = await generateCV(payload);
    setLoading(false);

    if (!response.success) {
      setError(response.error || "CV generation failed.");
      return;
    }

    const refreshed = await getState();
    setState(refreshed);
  };

  const cvContent = state?.cv?.content || "";
  const applicant = state?.applicant || {};

  return (
    <div className="page">
      <div className="page-header">
        <div>
          <span className="section-label">DOCUMENT GENERATION</span>
          <h1>CV Generator</h1>
          <p>Generate a structured CV using verified applicant information.</p>
        </div>
      </div>

      <div className="cv-layout">
        <section className="cv-control-card">
          <div className="card-heading">
            <div className="card-icon"><Sparkles size={20} /></div>
            <div>
              <h2>AI CV generation</h2>
              <p>The agent uses verified applicant information to prepare the CV.</p>
            </div>
          </div>

          <div className="cv-checklist">
            <div><CheckCircle2 size={17} /><span>Applicant identity</span></div>
            <div><CheckCircle2 size={17} /><span>Education information</span></div>
            <div><CheckCircle2 size={17} /><span>Experience information</span></div>
            <div><CheckCircle2 size={17} /><span>Verified documents</span></div>
          </div>

          <button className="primary-button full-width" onClick={handleGenerateCV} disabled={loading}>
            <Sparkles size={16} />
            {loading ? "Generating..." : "Generate CV"}
          </button>
        </section>

        <section className="cv-preview-card">
          <div className="cv-preview-header">
            <div>
              <span>PREVIEW</span>
              <h2>Applicant CV</h2>
            </div>

            {cvContent && (
              <button className="secondary-button" onClick={() => navigator.clipboard?.writeText(cvContent)}>
                <Download size={15} />
                Copy
              </button>
            )}
          </div>

          {cvContent ? (
            <div className="cv-document">
              <pre>{cvContent}</pre>
            </div>
          ) : (
            <div className="empty-preview">
              <FileUser size={35} />
              <h3>CV preview unavailable</h3>
              <p>{applicant.name ? "Generate the CV from the current applicant state." : "Complete and verify the applicant profile before generating the CV."}</p>
            </div>
          )}
        </section>
      </div>

      {error && <div className="error-box">{error}</div>}
    </div>
  );
}

export default CVGenerator;