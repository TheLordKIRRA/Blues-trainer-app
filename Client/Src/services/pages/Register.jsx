import { useState } from "react";
import { registerUser } from "../services/api";

export default function Register() {
  const [form, setForm] = useState({ email: "", username: "", password: "" });

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function submitRegister() {
    const res = await registerUser(form);
    if (res.token) window.location.href = "/dashboard";
  }

  return (
    <div>
      <h2>Create Account</h2>
      <input name="email" onChange={handleChange} placeholder="Email" />
      <input name="username" onChange={handleChange} placeholder="Username" />
      <input name="password" onChange={handleChange} type="password" placeholder="Password" />
      <button onClick={submitRegister}>Sign Up</button>
    </div>
  );
}
