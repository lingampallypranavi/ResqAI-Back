from flask import Blueprint, jsonify
from utils.roles import role_required

from models.user import User
from models.sos import SOSRequest
from models.shelter import Shelter
from models.rescue import RescueTeam

admin = Blueprint("admin", __name__)

# ===========================
# Dashboard
# ===========================
@admin.route("/dashboard", methods=["GET"])
@role_required("Admin")
def dashboard():

    return jsonify({
        "status": "success",
        "dashboard": {
            "total_users": User.query.count(),
            "total_sos_requests": SOSRequest.query.count(),
            "pending_sos": SOSRequest.query.filter_by(status="Pending").count(),
            "assigned_sos": SOSRequest.query.filter_by(status="Assigned").count(),
            "completed_sos": SOSRequest.query.filter_by(status="Completed").count(),
            "total_shelters": Shelter.query.count(),
            "total_rescue_teams": RescueTeam.query.count()
        }
    })


# ===========================
# View All Users
# ===========================
@admin.route("/users", methods=["GET"])
@role_required("Admin")
def get_users():

    users = User.query.all()

    data = []

    for user in users:
        data.append({
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "phone": user.phone
        })

    return jsonify({
        "status": "success",
        "count": len(data),
        "data": data
    })


# ===========================
# View All SOS Requests
# ===========================
@admin.route("/sos", methods=["GET"])
@role_required("Admin")
def get_sos():

    sos_list = SOSRequest.query.all()

    data = []

    for sos in sos_list:
        data.append({
            "sos_id": sos.sos_id,
            "user_id": sos.user_id,
            "disaster_type": sos.disaster_type,
            "priority": sos.priority,
            "status": sos.status,
            "latitude": sos.latitude,
            "longitude": sos.longitude
        })

    return jsonify({
        "status": "success",
        "count": len(data),
        "data": data
    })


# ===========================
# View All Shelters
# ===========================
@admin.route("/shelters", methods=["GET"])
@role_required("Admin")
def get_shelters():

    shelters = Shelter.query.all()

    data = []

    for shelter in shelters:
        data.append({
            "shelter_id": shelter.shelter_id,
            "name": shelter.name,
            "location": shelter.location,
            "capacity": shelter.capacity,
            "available_capacity": shelter.available_capacity
        })

    return jsonify({
        "status": "success",
        "count": len(data),
        "data": data
    })


# ===========================
# View All Rescue Teams
# ===========================
@admin.route("/rescue-teams", methods=["GET"])
@role_required("Admin")
def get_rescue_teams():

    teams = RescueTeam.query.all()

    data = []

    for team in teams:
        data.append({
            "rescue_id": team.rescue_id,
            "team_name": team.team_name,
            "location": team.location,
            "contact": team.contact,
            "status": team.status
        })

    return jsonify({
        "status": "success",
        "count": len(data),
        "data": data
    })