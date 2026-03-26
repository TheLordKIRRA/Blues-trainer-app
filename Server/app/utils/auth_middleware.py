from functools import wraps
from flask import request, jsonify
from app.utils.jwt_utils import decode_token
from app.models.user import User
from app.db.database import db

def require_auth(f):
@wraps(f)
def wrapper(*args, **kwargs):
auth_header = request.headers.get("Authorization", "")
if not auth_header.startswith("Bearer "):
return jsonify({"error": "Missing token"}), 401

token = auth_header.split(" ")[1]
decoded = decode_token(token)

if not decoded:
return jsonify({"error": "Invalid or expired token"}), 401

user = User.query.get(decoded["user_id"])
if not user:
return jsonify({"error": "User not found"}), 404

return f(user, *args, **kwargs)
return wrapper
