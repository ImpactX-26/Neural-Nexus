import { useEffect, useState } from "react";
import {
  Video,
  Upload,
  Mic,
  Brain,
  CheckCircle2,
  Clock
} from "lucide-react";
import { analyzeVideo, getState } from "./api";

function VideoAnalysis() {
  const [video, setVideo] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadState = async () => {
      const response = await getState();
      if (response?.video_analysis?.length) {
        setAnalysis(response.video_analysis[response.video_analysis.length - 1]);
      }
    };
    loadState();
  }, []);

  const handleVideo = async (event) => {
    const file = event.target.files?.[0];
    if (!file) return;

    setVideo(file);
    setLoading(true);
    setError("");

    const response = await analyzeVideo(file);
    setLoading(false);

    if (!response.success) {
      setError(response.error || "Video processing failed.");
      return;
    }

    setAnalysis(response.result);
    const refreshed = await getState();
    if (refreshed?.video_analysis?.length) {
      setAnalysis(refreshed.video_analysis[refreshed.video_analysis.length - 1]);
    }
  };

  return (
    <div className="page">
      <div className="page-header">
        <div>
          <span className="section-label">VIDEO INTELLIGENCE</span>
          <h1>Video Analysis</h1>
          <p>Process applicant video responses and extract structured information for the applicant journey.</p>
        </div>

        <div className="analysis-status">
          <Clock size={15} />
          {loading ? "Processing" : analysis ? "Completed" : "Waiting for video"}
        </div>
      </div>

      <div className="video-layout">
        <section className="upload-video-card">
          <div className="video-placeholder">
            <div className="video-icon"><Video size={30} /></div>
            <h2>{video ? video.name : "Upload applicant video"}</h2>
            <p>Supported formats include MP4, MOV and WebM.</p>

            <label className="primary-button">
              <Upload size={16} />
              {loading ? "Uploading..." : "Select Video"}
              <input type="file" hidden accept="video/*" onChange={handleVideo} />
            </label>
          </div>
        </section>

        <section className="analysis-card">
          <div className="card-heading">
            <div className="card-icon"><Brain size={20} /></div>
            <div>
              <h2>Analysis pipeline</h2>
              <p>Information extracted by the AI system</p>
            </div>
          </div>

          <div className="analysis-list">
            <div><Mic size={17} /><span>Speech extraction</span><strong>{analysis?.language?.detected || "Waiting"}</strong></div>
            <div><Brain size={17} /><span>Response analysis</span><strong>{analysis?.status || "Waiting"}</strong></div>
            <div><CheckCircle2 size={17} /><span>Structured insights</span><strong>{analysis ? "Available" : "Waiting"}</strong></div>
          </div>
        </section>
      </div>

      {error && <div className="error-box">{error}</div>}

      {analysis && (
        <section className="insight-card">
          <Brain size={20} />
          <div>
            <strong>Analysis result</strong>
            <p>{analysis.summary || "No summary available."}</p>
            <pre>{JSON.stringify(analysis, null, 2)}</pre>
          </div>
        </section>
      )}
    </div>
  );
}

export default VideoAnalysis;