from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
import bcrypt
from flask_jwt_extended import create_access_token

auth = Blueprint("auth", __name__)


# Test API
@auth.route("/test", methods=["GET"])
def test():
    return jsonify({
        "status": "success",
        "message": "Authentication API is Working!"
    })


# Register API
@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    # Check if email already exists
    existing_user = User.query.filter_by(email=data["email"]).first()

    if existing_user:
        return jsonify({
            "status": "error",
            "message": "Email already registered"
        }), 409

    # Hash password
    hashed_password = bcrypt.hashpw(
        data["password"].encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    # Create user
    new_user = User(
        name=data["name"],
        email=data["email"],
        password=hashed_password,
        role=data["role"],
        phone=data.get("phone")
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "User registered successfully"
    }), 201


# Login API
@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return jsonify({
            "status": "error",
            "message": "Invalid email or password"
        }), 401

    if not bcrypt.checkpw(
        data["password"].encode("utf-8"),
        user.password.encode("utf-8")
    ):
        return jsonify({
            "status": "error",
            "message": "Invalid email or password"
        }), 401

    # Generate JWT Token
    access_token = create_access_token(
        identity=str(user.user_id),
        additional_claims={
            "role": user.role,
            "name": user.name
        }
    )

    return jsonify({
        "status": "success",
        "message": "Login successful",
        "access_token": access_token,
        "user": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }), 200