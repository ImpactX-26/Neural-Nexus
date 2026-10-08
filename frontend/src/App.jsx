import { useState } from "react";
import Navbar from "../Navbar";
import Home from "../Home";
import ApplicantJourney from "../ApplicantJourney";
import Profile from "../Profile";
import Documents from "../Documents";
import Agent from "../Agent";
import VideoAnalysis from "../VideoAnalysis";
import Qualification from "../Qualification";
import CVGenerator from "../CVGenerator";
import NextSteps from "../NextSteps";
import DemoMode from "../DemoMode";

function App() {
  const [activePage, setActivePage] = useState("home");

  const renderPage = () => {
    switch (activePage) {
      case "home":
        return <Home setActivePage={setActivePage} />;

      case "journey":
        return <ApplicantJourney setActivePage={setActivePage} />;

      case "profile":
        return <Profile />;

      case "documents":
        return <Documents />;

      case "agent":
        return <Agent />;

      case "video":
        return <VideoAnalysis />;

      case "qualification":
        return <Qualification />;

      case "cv":
        return <CVGenerator />;

      case "next":
        return <NextSteps setActivePage={setActivePage} />;

      case "demo":
        return <DemoMode setActivePage={setActivePage} />;

      default:
        return <Home setActivePage={setActivePage} />;
    }
  };

  return (
    <div className="app">
      <Navbar
        activePage={activePage}
        setActivePage={setActivePage}
      />

      <main className="main-content">
        {renderPage()}
      </main>
    </div>
  );
}

export default App;