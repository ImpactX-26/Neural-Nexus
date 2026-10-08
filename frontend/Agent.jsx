import { useCallback, useEffect, useState } from "react";
import {
  getState,
  runAgent,
  runLearningAgent,
  runGermanyAgent,
  checkBackend,
  loadDemo,
} from "./api";

function Agent() {
  const [state, setState] = useState(null);
  const [agentResult, setAgentResult] = useState(null);
  const [backendStatus, setBackendStatus] = useState("Checking");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const initializeAgent = useCallback(async () => {
    await checkConnection();
    await refreshState();
  }, []);

  useEffect(() => {
    initializeAgent();
  }, [initializeAgent]);

  async function checkConnection() {
    const result = await checkBackend();

    if (result && result.success !== false) {
      setBackendStatus("Connected");
    } else {
      setBackendStatus("Offline");
    }
  }

  async function refreshState() {
    const result = await getState();

    if (result && result.success !== false) {
      setState(result.state || result);
    }
  }

  async function handleRunAgent() {
    setLoading(true);
    setError("");
    setAgentResult(null);

    try {
      const result = await runLearningAgent({
        goal: message || "Analyze my applicant journey and determine the next required action.",
        topic: "Germany applicant journey",
        skill_level: "Intermediate",
        purpose: "Germany application support",
        available_time: "Flexible",
        learning_style: "Mixed",
      });

      if (result?.success === false) {
        setError(result.error || "Agent execution failed.");
        return;
      }

      setAgentResult(result);

      if (result.state) {
        setState(result.state);
      } else {
        await refreshState();
      }
    } catch (err) {
      setError(err.message || "Unable to run LearnoryX Agent.");
    } finally {
      setLoading(false);
    }
  }

  async function handleLoadDemo() {
    setLoading(true);
    setError("");

    try {
      const result = await loadDemo();

      if (result?.success === false) {
        setError(result.error || "Unable to load demo.");
        return;
      }

      await refreshState();
      setMessage("Demo applicant loaded. The agent is ready.");
    } catch (err) {
      setError(err.message || "Unable to load demo.");
    } finally {
      setLoading(false);
    }
  }

  const currentStage =
    state?.current_stage ||
    state?.journey_progress?.current_stage ||
    state?.stage ||
    "Applicant Assessment";

  const agentStatus =
    agentResult?.agent_status ||
    state?.agent_status ||
    "READY";

  const currentAction =
    agentResult?.action ||
    agentResult?.next_action ||
    state?.last_action ||
    "Waiting for agent execution";

  const nextAction =
    agentResult?.next_action ||
    state?.next_action ||
    "Start the LearnoryX Agent";

  const decision =
    agentResult?.decision ||
    state?.decision ||
    "No decision available yet";

  const trace =
    agentResult?.trace ||
    agentResult?.raw?.agent_trace ||
    state?.agent_history ||
    state?.history ||
    [];

  const documents = state?.documents || [];
  const verifiedDocuments =
    state?.document_verification ||
    state?.verified_documents ||
    [];

  const profile =
    state?.applicant_profile ||
    state?.profile ||
    {};

  const qualification =
    state?.qualification ||
    {};

  const getStatusClass = (status) => {
    const value = String(status || "").toLowerCase();

    if (
      value.includes("complete") ||
      value.includes("success") ||
      value.includes("pass") ||
      value.includes("ready")
    ) {
      return "agent-status-success";
    }

    if (
      value.includes("thinking") ||
      value.includes("execut") ||
      value.includes("verif") ||
      value.includes("working")
    ) {
      return "agent-status-working";
    }

    if (
      value.includes("error") ||
      value.includes("fail")
    ) {
      return "agent-status-error";
    }

    if (value.includes("wait")) {
      return "agent-status-waiting";
    }

    return "agent-status-idle";
  };

  const formatLabel = (value) => {
    if (!value) return "Not available";

    return String(value)
      .replaceAll("_", " ")
      .replace(/\b\w/g, (char) => char.toUpperCase());
  };

  return (
    <div className="agent-page">

      {/* HEADER */}
      <div className="agent-header">
        <div>
          <div className="agent-eyebrow">
            LEARNORYX INTELLIGENCE
          </div>

          <h1>LearnoryX Agent</h1>

          <p>
            Autonomous applicant journey intelligence
          </p>
        </div>

        <div className="agent-header-status">
          <span
            className={`status-dot ${
              backendStatus === "Connected"
                ? "status-online"
                : "status-offline"
            }`}
          />

          <span>
            Backend {backendStatus}
          </span>
        </div>
      </div>

      {/* TOP STATUS */}
      <div className="agent-top-grid">

        <div className="agent-status-card">
          <div className="card-label">
            AGENT STATUS
          </div>

          <div className="agent-status-row">
            <div
              className={`agent-status-indicator ${getStatusClass(
                agentStatus
              )}`}
            />

            <strong>
              {formatLabel(agentStatus)}
            </strong>
          </div>

          <div className="agent-status-description">
            {loading
              ? "The autonomous agent is analyzing the applicant state and executing the required workflow."
              : "The agent is ready to inspect the applicant journey and determine the next action."}
          </div>
        </div>

        <div className="agent-objective-card">
          <div className="card-label">
            CURRENT STAGE
          </div>

          <h2>
            {formatLabel(currentStage)}
          </h2>

          <p>
            The agent is monitoring the applicant journey and
            determining what needs to happen next.
          </p>
        </div>

        <div className="agent-connection-card">
          <div className="card-label">
            AUTONOMOUS MODE
          </div>

          <div className="autonomous-badge">
            <span className="autonomous-dot" />
            ACTIVE
          </div>

          <p>
            State-driven execution enabled
          </p>
        </div>

      </div>

      {/* MAIN GRID */}
      <div className="agent-main-grid">

        {/* LEFT */}
        <div className="agent-main-column">

          {/* DECISION CONTEXT */}
          <section className="agent-card decision-card">

            <div className="section-header">
              <div>
                <div className="card-label">
                  DECISION CONTEXT
                </div>

                <h2>What the agent decided</h2>
              </div>

              <div className="decision-tag">
                {formatLabel(decision)}
              </div>
            </div>

            <div className="decision-content">
              <div className="decision-icon">
                AI
              </div>

              <div>
                <h3>
                  {formatLabel(currentAction)}
                </h3>

                <p>
                  {agentResult?.reasoning ||
                    agentResult?.result ||
                    "The agent will inspect the current applicant state and select the next valid operation."}
                </p>
              </div>
            </div>

          </section>

          {/* EXECUTION PIPELINE */}
          <section className="agent-card">

            <div className="section-header">
              <div>
                <div className="card-label">
                  AUTONOMOUS EXECUTION
                </div>

                <h2>Agent pipeline</h2>
              </div>
            </div>

            <div className="agent-pipeline">

              <PipelineStep
                number="01"
                title="Observe"
                description="Inspect applicant state"
                active={loading}
              />

              <PipelineLine />

              <PipelineStep
                number="02"
                title="Decide"
                description="Determine next action"
                active={loading}
              />

              <PipelineLine />

              <PipelineStep
                number="03"
                title="Act"
                description="Execute selected tool"
                active={loading}
              />

              <PipelineLine />

              <PipelineStep
                number="04"
                title="Verify"
                description="Validate operation"
                active={loading}
              />

              <PipelineLine />

              <PipelineStep
                number="05"
                title="Update"
                description="Update applicant state"
                active={loading}
              />

            </div>

          </section>

          {/* LIVE TRACE */}
          <section className="agent-card">

            <div className="section-header">
              <div>
                <div className="card-label">
                  LIVE AGENT ACTIVITY
                </div>

                <h2>Execution trace</h2>
              </div>

              <div className="trace-live">
                <span />
                LIVE
              </div>
            </div>

            <div className="agent-trace">

              {trace.length === 0 ? (
                <div className="trace-empty">
                  <div className="trace-empty-icon">
                    LY
                  </div>

                  <h3>Agent ready</h3>

                  <p>
                    Run the agent to begin autonomous applicant
                    analysis.
                  </p>
                </div>
              ) : (
                trace.map((item, index) => (
                  <TraceItem
                    key={index}
                    item={item}
                    index={index}
                  />
                ))
              )}

            </div>

          </section>

        </div>

        {/* RIGHT */}
        <div className="agent-side-column">

          {/* RUN AGENT */}
          <section className="agent-control-card">

            <div className="agent-mini-logo">
              LY
            </div>

            <div className="card-label">
              LEARNORYX AGENT
            </div>

            <h2>
              Autonomous Mode
            </h2>

            <p>
              Let the agent inspect the applicant state,
              select tools, execute actions, verify results,
              and determine the next step.
            </p>

            <button
              className="run-agent-button"
              onClick={handleRunAgent}
              disabled={loading}
            >
              {loading ? (
                <>
                  <span className="button-spinner" />
                  Agent Working...
                </>
              ) : (
                <>
                  Run LearnoryX Agent
                  <span className="button-arrow">
                    →
                  </span>
                </>
              )}
            </button>

            <button
              className="demo-button"
              onClick={handleLoadDemo}
              disabled={loading}
            >
              Load Demo Applicant
            </button>

          </section>

          {/* NEXT ACTION */}
          <section className="agent-card next-action-card">

            <div className="card-label">
              NEXT ACTION
            </div>

            <h2>
              {formatLabel(nextAction)}
            </h2>

            <p>
              The next operation determined from the current
              applicant state.
            </p>

            <div className="next-action-line" />

            <span className="next-action-status">
              Agent Recommendation
            </span>

          </section>

          {/* APPLICANT STATE */}
          <section className="agent-card">

            <div className="card-label">
              APPLICANT STATE
            </div>

            <h2>Current state</h2>

            <div className="state-list">

              <StateRow
                label="Profile"
                value={
                  profile?.name
                    ? "Complete"
                    : "Incomplete"
                }
              />

              <StateRow
                label="Education"
                value={
                  state?.education ||
                  profile?.education ||
                  "Not available"
                }
              />

              <StateRow
                label="Documents"
                value={`${documents.length} uploaded`}
              />

              <StateRow
                label="Verified"
                value={
                  Array.isArray(verifiedDocuments)
                    ? `${verifiedDocuments.length} verified`
                    : "Processing"
                }
              />

              <StateRow
                label="Qualification"
                value={
                  qualification?.status ||
                  "Pending"
                }
              />

              <StateRow
                label="Target"
                value={
                  state?.target_pathway ||
                  profile?.target ||
                  "Not selected"
                }
              />

            </div>

          </section>

          {/* ERROR */}
          {error && (
            <section className="agent-error-card">

              <div className="error-title">
                Agent Action Failed
              </div>

              <p>{error}</p>

              <button
                onClick={handleRunAgent}
                disabled={loading}
              >
                Retry
              </button>

            </section>
          )}

          {/* MESSAGE */}
          {message && (
            <div className="agent-success-message">
              {message}
            </div>
          )}

        </div>

      </div>

    </div>
  );
}


/* -----------------------------
   PIPELINE COMPONENT
----------------------------- */

function PipelineStep({
  number,
  title,
  description,
  active,
}) {
  return (
    <div className={`pipeline-step ${active ? "active" : ""}`}>

      <div className="pipeline-number">
        {number}
      </div>

      <div>
        <strong>{title}</strong>

        <span>{description}</span>
      </div>

    </div>
  );
}


function PipelineLine() {
  return (
    <div className="pipeline-line" />
  );
}


/* -----------------------------
   TRACE COMPONENT
----------------------------- */

function TraceItem({ item, index }) {

  const status =
    item?.status ||
    item?.state ||
    "completed";

  const action =
    item?.action ||
    item?.tool ||
    item?.decision ||
    "Agent action";

  const result =
    item?.result ||
    item?.reasoning ||
    item?.message ||
    "";

  return (
    <div className="trace-item">

      <div className="trace-marker">
        <span />
      </div>

      <div className="trace-content">

        <div className="trace-top">

          <span className="trace-step">
            STEP {String(index + 1).padStart(2, "0")}
          </span>

          <span
            className={`trace-status ${getTraceStatusClass(
              status
            )}`}
          >
            {String(status).toUpperCase()}
          </span>

        </div>

        <h3>
          {formatTraceLabel(action)}
        </h3>

        {result && (
          <p>
            {typeof result === "string"
              ? result
              : JSON.stringify(result)}
          </p>
        )}

      </div>

    </div>
  );
}


function getTraceStatusClass(status) {

  const value = String(status || "").toLowerCase();

  if (
    value.includes("success") ||
    value.includes("complete") ||
    value.includes("pass")
  ) {
    return "trace-success";
  }

  if (
    value.includes("running") ||
    value.includes("execut") ||
    value.includes("working")
  ) {
    return "trace-running";
  }

  if (
    value.includes("fail") ||
    value.includes("error")
  ) {
    return "trace-error";
  }

  return "trace-neutral";
}


function formatTraceLabel(value) {

  if (!value) return "Agent action";

  return String(value)
    .replaceAll("_", " ")
    .replace(/\b\w/g, (char) => char.toUpperCase());
}


/* -----------------------------
   STATE ROW
----------------------------- */

function StateRow({ label, value }) {

  return (
    <div className="state-row">

      <span>
        {label}
      </span>

      <strong>
        {formatTraceLabel(value)}
      </strong>

    </div>
  );
}

export default Agent;