import { useEffect, useState } from "react";
import { getPracticeSessions } from "../services/api";

export default function Dashboard() {
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    async function load() {
      const token = localStorage.getItem("token");
      const data = await getPracticeSessions(token);
      setSessions(data);
    }
    load();
  }, []);

  return (
    <div>
      <h1>Your Practice Sessions</h1>
      <a href="/new-session">Add New Session</a>
      <ul>
        {sessions.map((s) => (
          <li key={s.id}>
            {s.activity_type} — {s.duration_minutes} minutes
          </li>
        ))}
      </ul>
    </div>
  );
}
