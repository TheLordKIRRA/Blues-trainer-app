from flask import Blueprint, request, jsonify
from app.models.practice_session import PracticeSession
from app.db.database import db
from app.utils.auth_middleware import require_auth
from app.schemas.practice_schema import PracticeSessionSchema

practice_bp = Blueprint("practice", __name__)

@practice_bp.post("/")
@require_auth
def create_session(user):
data = PracticeSessionSchema().load(request.json)
session = PracticeSession(
user_id=user.id,
duration_minutes=data["duration_minutes"],
notes=data.get("notes"),
activity_type=data["activity_type"]
)
db.session.add(session)
db.session.commit()
return jsonify(session.to_dict()), 201

@practice_bp.get("/")
@require_auth
def list_sessions(user):
sessions = PracticeSession.query.filter_by(user_id=user.id).all()
return jsonify([s.to_dict() for s in sessions])
