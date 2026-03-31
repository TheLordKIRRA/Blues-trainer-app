import { useState } from "react";
import { loginUser } from "../services/api";

export default function Login() {
  const [form, setForm] = useState({ email: "", password: "" });

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function submitLogin() {
    const res = await loginUser(form);
    if (res.token) {
      localStorage.setItem("token", res.token);
      window.location.href = "/dashboard";
    }
  }

  return (
    <div>
      <h2>Login</h2>
      <input name="email" onChange={handleChange} placeholder="Email" />
      <input name="password" onChange={handleChange} type="password" placeholder="Password" />
      <button onClick={submitLogin}>Login</button>
    </div>
  );
}
