import {
  LayoutDashboard,
  Route,
  UserRound,
  FileText,
  Bot,
  Video,
  GraduationCap,
  FileUser,
  ArrowRight,
  PlayCircle
} from "lucide-react";

function Navbar({ activePage, setActivePage }) {
  const navItems = [
    {
      id: "home",
      label: "Home",
      icon: LayoutDashboard
    },
    {
      id: "journey",
      label: "Applicant Journey",
      icon: Route
    },
    {
      id: "profile",
      label: "Profile",
      icon: UserRound
    },
    {
      id: "documents",
      label: "Documents",
      icon: FileText
    },
    {
      id: "agent",
      label: "AI Agent",
      icon: Bot
    },
    {
      id: "video",
      label: "Video Analysis",
      icon: Video
    },
    {
      id: "qualification",
      label: "Qualification",
      icon: GraduationCap
    },
    {
      id: "cv",
      label: "CV Generator",
      icon: FileUser
    },
    {
      id: "next",
      label: "Next Steps",
      icon: ArrowRight
    },
    {
      id: "demo",
      label: "Demo Mode",
      icon: PlayCircle
    }
  ];

  return (
    <aside className="sidebar">
      <div className="brand-section">
        <div className="brand-mark">LX</div>

        <div className="brand-text">
          <h2>LearnoryX</h2>
          <span>Agentic AI</span>
        </div>
      </div>

      <div className="agent-status">
        <div className="status-indicator"></div>

        <div>
          <strong>Agent Online</strong>
          <span>Decision engine ready</span>
        </div>
      </div>

      <nav className="navigation">
        {navItems.map((item) => {
          const Icon = item.icon;

          return (
            <button
              key={item.id}
              className={`nav-item ${
                activePage === item.id ? "active" : ""
              }`}
              onClick={() => setActivePage(item.id)}
            >
              <Icon size={18} />
              <span>{item.label}</span>
            </button>
          );
        })}
      </nav>

      <div className="sidebar-footer">
        <div className="journey-mini">
          <div className="journey-mini-header">
            <span>Journey Progress</span>
            <strong>0%</strong>
          </div>

          <div className="progress-track">
            <div className="progress-fill"></div>
          </div>
        </div>

        <p>LearnoryX v1.0</p>
      </div>
    </aside>
  );
}

export default Navbar;