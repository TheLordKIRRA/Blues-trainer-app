from flask import Blueprint, request, jsonify
from app.models.user import User
from app.schemas.auth_schema import RegisterSchema, LoginSchema
from app.utils.auth import create_jwt
from app.db.database import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    errors = RegisterSchema().validate(data)

    if errors:
        return jsonify(errors), 400

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already registered"}), 409

    user = User(
        username=data["username"],
        email=data["email"]
    )
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    token = create_jwt(user.id)
    return jsonify({"token": token}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    errors = LoginSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    user = User.query.filter_by(username=data["username"]).first()

    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_jwt(user.id)
    return jsonify({"token": token}), 200
