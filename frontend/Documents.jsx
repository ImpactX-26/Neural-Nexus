import { useEffect, useState } from "react";
import {
  Upload,
  FileText,
  CheckCircle2,
  AlertCircle,
  Clock,
  ShieldCheck
} from "lucide-react";
import { getState, uploadDocument } from "./api";

function Documents() {
  const [documents, setDocuments] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadDocuments = async () => {
      const response = await getState();
      if (response?.documents) {
        setDocuments(response.documents);
      }
    };
    loadDocuments();
  }, []);

  const handleUpload = async (event) => {
    const files = Array.from(event.target.files || []);
    if (!files.length) return;

    setUploading(true);
    setError("");

    const uploaded = [];
    for (const file of files) {
      const response = await uploadDocument(file);
      if (response?.success) {
        uploaded.push({
          id: `${file.name}-${Date.now()}`,
          name: response.filename || file.name,
          size: `${(file.size / 1024 / 1024).toFixed(2)} MB`,
          status: "Uploaded",
          verification: response.result?.verification?.status || "pending",
          confidence: response.result?.verification?.confidence || 0,
          extracted_text: response.result?.extracted_text || ""
        });
      } else {
        setError(response?.error || "Document upload failed.");
      }
    }

    if (uploaded.length) {
      const refreshed = await getState();
      if (refreshed?.documents) setDocuments(refreshed.documents);
    }

    setUploading(false);
    event.target.value = "";
  };

  const visibleDocuments = documents.length ? documents : [];

  return (
    <div className="page">
      <div className="page-header">
        <div>
          <span className="section-label">DOCUMENT INTELLIGENCE</span>
          <h1>Documents</h1>
          <p>Upload applicant documents for extraction, analysis and verification.</p>
        </div>

        <label className="upload-button">
          <Upload size={17} />
          {uploading ? "Uploading..." : "Upload Documents"}
          <input type="file" multiple accept=".pdf,.doc,.docx,.txt,.png,.jpg,.jpeg" onChange={handleUpload} />
        </label>
      </div>

      <div className="document-info-grid">
        <div className="info-card"><FileText size={19} /><div><strong>Extraction</strong><span>Structured information</span></div></div>
        <div className="info-card"><ShieldCheck size={19} /><div><strong>Verification</strong><span>Consistency checks</span></div></div>
        <div className="info-card"><CheckCircle2 size={19} /><div><strong>Applicant State</strong><span>Verified information</span></div></div>
      </div>

      {error && <div className="error-box">{error}</div>}

      <section className="document-card">
        <div className="card-heading">
          <div>
            <h2>Applicant documents</h2>
            <p>LearnoryX determines which documents are useful based on the current applicant state.</p>
          </div>
        </div>

        <div className="document-list">
          {visibleDocuments.length === 0 ? (
            <div className="empty-preview">No documents uploaded yet.</div>
          ) : visibleDocuments.map((document) => (
            <div className="document-row" key={document.filename || document.id || document.path || Math.random()}>
              <div className="document-main">
                <div className="document-icon"><FileText size={20} /></div>
                <div>
                  <strong>{document.filename || document.name || "Document"}</strong>
                  <span>{document.path ? document.path.split("/").slice(-1)[0] : document.size || "Uploaded"}</span>
                </div>
              </div>

              <div className="document-status">
                {document.verification?.status === "strong_match" || document.verification_status === "strong_match" ? (
                  <span className="status-pill success"><CheckCircle2 size={13} /> Verified</span>
                ) : document.verification?.status || document.verification_status ? (
                  <span className="status-pill warning"><AlertCircle size={13} /> {document.verification?.status || document.verification_status}</span>
                ) : (
                  <span className="status-pill processing"><Clock size={13} /> Processing</span>
                )}

                {document.verification?.confidence !== undefined && (
                  <span className="verification-pill">Confidence: {document.verification.confidence}</span>
                )}
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="agent-note">
        <ShieldCheck size={20} />
        <div>
          <strong>Verification happens before decisions</strong>
          <p>Extracted information should not automatically become trusted applicant information. LearnoryX uses a verification layer before important data is added to the applicant state.</p>
        </div>
      </section>
    </div>
  );
}

export default Documents;