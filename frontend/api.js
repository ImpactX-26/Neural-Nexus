const API_BASE_URL = "http://127.0.0.1:8000";

async function request(endpoint, options = {}) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, options);

    const contentType = response.headers.get("content-type") || "";

    let data;

    if (contentType.includes("application/json")) {
      data = await response.json();
    } else {
      const text = await response.text();
      data = {
        detail: text || "Backend request failed",
      };
    }

    if (!response.ok) {
      throw new Error(
        data.detail || data.error || "Backend request failed"
      );
    }

    return data;
  } catch (error) {
    console.error(`API Error: ${endpoint}`, error);

    return {
      success: false,
      error:
        error.message || "Unable to connect to LearnoryX backend",
    };
  }
}


/* ================================
   BACKEND HEALTH
================================ */

export async function checkBackend() {
  return request("/health");
}


/* ================================
   APPLICANT STATE
================================ */

export async function getState() {
  return request("/api/state");
}


/* ================================
   MAIN AGENT
================================ */

export async function runAgent(message = "") {
  return request("/api/agent", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message,
    }),
  });
}


/* ================================
   GERMANY APPLICANT AGENT
================================ */

export async function runGermanyAgent(profile = {}) {
  return request("/api/germany/applicant", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(profile),
  });
}


/* ================================
   LEARNORYX AUTONOMOUS LEARNING AGENT
================================ */

export async function runLearningAgent(data) {
  return request("/api/learning-agent", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
}


/* ================================
   PROFILE
================================ */

export async function saveProfile(profile) {
  return request("/api/profile", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(profile),
  });
}


/* ================================
   DOCUMENT UPLOAD
================================ */

export async function uploadDocument(file) {
  const formData = new FormData();

  formData.append("file", file);

  return request("/api/documents/upload", {
    method: "POST",
    body: formData,
  });
}


/* ================================
   VIDEO ANALYSIS
================================ */

export async function analyzeVideo(file) {
  const formData = new FormData();

  formData.append("file", file);

  return request("/api/video/analyze", {
    method: "POST",
    body: formData,
  });
}


/* ================================
   QUALIFICATION
================================ */

export async function evaluateQualification(data) {
  return request("/api/qualification", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
}


/* ================================
   CV GENERATOR
================================ */

export async function generateCV(data) {
  return request("/api/cv", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
}


/* ================================
   NEXT STEPS
================================ */

export async function getNextSteps() {
  return request("/api/next-steps");
}


/* ================================
   DEMO MODE
================================ */

export async function loadDemo() {
  return request("/api/demo", {
    method: "POST",
  });
}


/* ================================
   RESET APPLICANT
================================ */

export async function resetApplicant() {
  return request("/api/reset", {
    method: "POST",
  });
}