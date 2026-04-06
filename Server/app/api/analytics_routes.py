from flask import Blueprint, jsonify
from app.models.pracitce_session import PracticeSession  # Note: Filename has a typo ("pracitce" instead of "practice")
from app.services.analytics_services import calculate_total_minutes, calculate_average_duration
from app.utils.auth_middleware import require_auth

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/total-minutes/<int:user_id>", methods=["GET"])
@require_auth
def get_total_minutes(user_id):
    # Retrieve all sessions for the user
    sessions = PracticeSession.query.filter_by(user_id=user_id).all()
    total = calculate_total_minutes(sessions)
    return jsonify({"total_minutes": total})

@analytics_bp.route("/average-duration/<int:user_id>", methods=["GET"])
@require_auth
def get_average_duration(user_id):
    # Retrieve all sessions for the user
    sessions = PracticeSession.query.filter_by(user_id=user_id).all()
    avg = calculate_average_duration(sessions)
    return jsonify({"average_duration": avg})