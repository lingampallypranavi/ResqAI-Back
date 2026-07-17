from flask import Blueprint, request, jsonify
from extensions import db
from models.rescue import RescueTeam
from models.sos import SOSRequest
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.roles import role_required


rescue = Blueprint("rescue", __name__)


# Test API
@rescue.route("/test", methods=["GET"])
def test():
    return jsonify({
        "status": "success",
        "message": "Rescue API is Working!"
    })


# Create Rescue Team (Admin only)
@rescue.route("/create", methods=["POST"])
@role_required("Admin")
def create_rescue_team():

    data = request.get_json()

    new_team = RescueTeam(
        user_id=data["user_id"],
        team_name=data["team_name"],
        location=data["location"],
        contact=data["contact"]
    )

    db.session.add(new_team)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Rescue team created successfully",
        "rescue_id": new_team.rescue_id
    }), 201


# Get all rescue teams
@rescue.route("/all", methods=["GET"])
@jwt_required()
def get_all_rescue():

    teams = RescueTeam.query.all()

    result = []

    for team in teams:
        result.append({
            "rescue_id": team.rescue_id,
            "team_name": team.team_name,
            "location": team.location,
            "contact": team.contact,
            "status": team.status
        })

    return jsonify({
        "status": "success",
        "data": result
    })

# View Pending SOS Requests
@rescue.route("/pending", methods=["GET"])
@role_required("Rescue Team")
def pending_sos():

    pending = SOSRequest.query.filter_by(status="Pending").all()

    result = []

    for sos in pending:
        result.append({
            "sos_id": sos.sos_id,
            "user_id": sos.user_id,
            "disaster_type": sos.disaster_type,
            "latitude": sos.latitude,
            "longitude": sos.longitude,
            "priority": sos.priority,
            "status": sos.status,
            "created_at": sos.created_at.strftime("%Y-%m-%d %H:%M:%S")
        })

    return jsonify({
        "status": "success",
        "count": len(result),
        "data": result
    })

# Update rescue team status
@rescue.route("/status/<int:rescue_id>", methods=["PUT"])
@role_required("Rescue Team")
def update_status(rescue_id):

    team = RescueTeam.query.get(rescue_id)

    if not team:
        return jsonify({
            "status": "error",
            "message": "Rescue team not found"
        }), 404

    data = request.get_json()

    team.status = data.get(
        "status",
        team.status
    )

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Status updated"
    })
@rescue.route("/accept/<int:sos_id>", methods=["PUT"])
@role_required("Rescue Team")
def accept_sos(sos_id):

    sos = SOSRequest.query.get(sos_id)

    if not sos:
        return jsonify({
            "status": "error",
            "message": "SOS not found"
        }), 404

    sos.status = "Assigned"

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "SOS accepted successfully"
    })
@rescue.route("/complete/<int:sos_id>", methods=["PUT"])
@role_required("Rescue Team")
def complete_sos(sos_id):

    sos = SOSRequest.query.get(sos_id)

    if not sos:
        return jsonify({
            "status": "error",
            "message": "SOS not found"
        }), 404

    sos.status = "Completed"

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Rescue completed successfully"
    })