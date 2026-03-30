const API_URL = "http://localhost:5000/api";

export async function registerUser(data) {
const res = await fetch(`${API_URL}/auth/register`, {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(data),
});
return res.json();
}

export async function loginUser(data) {
const res = await fetch(`${API_URL}/auth/login`, {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(data),
});
return res.json();
}

export async function createPracticeSession(token, data) {
const res = await fetch(`${API_URL}/practice/`, {
method: "POST",
headers: {
"Content-Type": "application/json",
Authorization: `Bearer ${token}`,
},
body: JSON.stringify(data),
});
return res.json();
}

export async function getPracticeSessions(token) {
const res = await fetch(`${API_URL}/practice/`, {
headers: { Authorization: `Bearer ${token}` },
});
return res.json();
}
