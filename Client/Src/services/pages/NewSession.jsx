import { useState } from "react";
import { createPracticeSession } from "../services/api";

export default function NewSession() {
  const [form, setForm] = useState({
    duration_minutes: "",
    activity_type: "",
    notes: ""
  });

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function save() {
    const token = localStorage.getItem("token");
    await createPracticeSession(token, form);
    window.location.href = "/dashboard";
  }

  return (
    <div>
      <h2>Log Practice Session</h2>
      <input name="duration_minutes" onChange={handleChange} placeholder="Duration" />
      <input name="activity_type" onChange={handleChange} placeholder="Activity" />
      <textarea name="notes" onChange={handleChange} placeholder="Notes" />
      <button onClick={save}>Save</button>
    </div>
  );
}
