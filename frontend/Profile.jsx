import { useEffect, useState } from "react";
import {
  UserRound,
  GraduationCap,
  BriefcaseBusiness,
  MapPin,
  Target,
  Save,
  CheckCircle2
} from "lucide-react";
import { getState, saveProfile } from "./api";

function Profile() {
  const [saved, setSaved] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [profile, setProfile] = useState({
    name: "",
    email: "",
    phone: "",
    country: "India",
    education: "",
    degree: "",
    field: "",
    experience: "",
    target: "",
    german_level: "",
    english_level: ""
  });

  useEffect(() => {
    const loadProfile = async () => {
      const response = await getState();
      if (response?.applicant) {
        setProfile({
          ...response.applicant,
          degree: response.applicant.degree || "",
          field: response.applicant.field || "",
          target: response.applicant.target || "",
          german_level: response.applicant.german_level || "",
          english_level: response.applicant.english_level || ""
        });
      }
    };
    loadProfile();
  }, []);

  const updateField = (field, value) => {
    setProfile((current) => ({ ...current, [field]: value }));
    setSaved(false);
    setError("");
  };

  const handleSaveProfile = async () => {
    setLoading(true);
    setError("");

    const response = await saveProfile(profile);
    setLoading(false);

    if (!response.success) {
      setError(response.error || "Profile could not be saved.");
      return;
    }

    setSaved(true);
    const refreshed = await getState();
    if (refreshed?.applicant) setProfile(refreshed.applicant);
  };

  return (
    <div className="page">
      <div className="page-header">
        <div>
          <span className="section-label">APPLICANT PROFILE</span>
          <h1>Build your profile</h1>
          <p>LearnoryX progressively structures your information and updates the applicant state as new data becomes available.</p>
        </div>

        {saved && (
          <div className="success-badge">
            <CheckCircle2 size={15} />
            Profile saved
          </div>
        )}
      </div>

      <div className="form-layout">
        <section className="form-card">
          <div className="card-heading">
            <div className="card-icon"><UserRound size={20} /></div>
            <div>
              <h2>Personal information</h2>
              <p>Basic applicant information</p>
            </div>
          </div>

          <div className="form-grid">
            <label>
              Full name
              <input value={profile.name} onChange={(e) => updateField("name", e.target.value)} placeholder="Enter your full name" />
            </label>
            <label>
              Email address
              <input type="email" value={profile.email} onChange={(e) => updateField("email", e.target.value)} placeholder="you@example.com" />
            </label>
            <label>
              Phone number
              <input value={profile.phone} onChange={(e) => updateField("phone", e.target.value)} placeholder="+91" />
            </label>
            <label>
              Current country
              <select value={profile.country} onChange={(e) => updateField("country", e.target.value)}>
                <option>India</option>
                <option>Germany</option>
                <option>Other</option>
              </select>
            </label>
          </div>
        </section>

        <section className="form-card">
          <div className="card-heading">
            <div className="card-icon"><GraduationCap size={20} /></div>
            <div>
              <h2>Education</h2>
              <p>Your academic background</p>
            </div>
          </div>

          <div className="form-grid">
            <label>
              Highest qualification
              <input value={profile.education} onChange={(e) => updateField("education", e.target.value)} placeholder="Bachelor's degree" />
            </label>
            <label>
              Degree name
              <input value={profile.degree || ""} onChange={(e) => updateField("degree", e.target.value)} placeholder="B.Tech / BSc / MBA" />
            </label>
            <label>
              Field of study
              <input value={profile.field || ""} onChange={(e) => updateField("field", e.target.value)} placeholder="Computer Science" />
            </label>
            <label>
              German level
              <input value={profile.german_level || ""} onChange={(e) => updateField("german_level", e.target.value)} placeholder="A2 / B1 / B2" />
            </label>
            <label>
              English level
              <input value={profile.english_level || ""} onChange={(e) => updateField("english_level", e.target.value)} placeholder="B2 / C1" />
            </label>
            <label>
              Target pathway
              <input value={profile.target || ""} onChange={(e) => updateField("target", e.target.value)} placeholder="Study / Vocational Training / Employment" />
            </label>
          </div>
        </section>

        <section className="form-card">
          <div className="card-heading">
            <div className="card-icon"><BriefcaseBusiness size={20} /></div>
            <div>
              <h2>Experience</h2>
              <p>Professional background</p>
            </div>
          </div>

          <label>
            Experience summary
            <textarea rows="5" value={profile.experience} onChange={(e) => updateField("experience", e.target.value)} placeholder="Describe your experience, internships, projects or relevant skills." />
          </label>
        </section>

        <div className="form-actions">
          <div className="location-note">
            <MapPin size={16} />
            Applicant journey starts from India
          </div>

          <button className="primary-button" onClick={handleSaveProfile} disabled={loading}>
            <Save size={16} />
            {loading ? "Saving..." : "Save Profile"}
          </button>
        </div>

        {error && <div className="error-box">{error}</div>}
      </div>
    </div>
  );
}

export default Profile;