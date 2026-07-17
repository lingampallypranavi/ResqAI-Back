from flask import Blueprint, request, jsonify
from extensions import db
from models.sos import SOSRequest
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from utils.roles import role_required

sos = Blueprint("sos", __name__)


# Test API
@sos.route("/test", methods=["GET"])
def test():
    return jsonify({
        "status": "success",
        "message": "SOS API is Working!"
    })


# Create SOS
@sos.route("/create", methods=["POST"])
@role_required("Victim")
def create_sos():

    data = request.get_json()

    new_sos = SOSRequest(
        user_id=data.get("user_id"),
        disaster_type=data.get("disaster_type"),
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
        priority=data.get("priority", "Medium")
    )

    db.session.add(new_sos)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "SOS created successfully",
        "sos_id": new_sos.sos_id
    }), 201


# Get All SOS
@sos.route("/all", methods=["GET"])
def get_all_sos():

    sos_requests = SOSRequest.query.all()

    result = []

    for sos_item in sos_requests:
        result.append({
            "sos_id": sos_item.sos_id,
            "user_id": sos_item.user_id,
            "disaster_type": sos_item.disaster_type,
            "latitude": sos_item.latitude,
            "longitude": sos_item.longitude,
            "priority": sos_item.priority,
            "status": sos_item.status,
            "created_at": sos_item.created_at.strftime("%Y-%m-%d %H:%M:%S")
        })

    return jsonify({
        "status": "success",
        "count": len(result),
        "data": result
    }), 200
# Get SOS by ID
@sos.route("/<int:sos_id>", methods=["GET"])
def get_sos_by_id(sos_id):

    sos_request = SOSRequest.query.get(sos_id)

    if not sos_request:
        return jsonify({
            "status": "error",
            "message": "SOS request not found"
        }), 404

    return jsonify({
        "status": "success",
        "data": {
            "sos_id": sos_request.sos_id,
            "user_id": sos_request.user_id,
            "disaster_type": sos_request.disaster_type,
            "latitude": sos_request.latitude,
            "longitude": sos_request.longitude,
            "priority": sos_request.priority,
            "status": sos_request.status,
            "created_at": sos_request.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
    }), 200
# Update SOS Status
@sos.route("/update/<int:sos_id>", methods=["PUT"])
@role_required("Admin", "Rescue Team")
def update_sos(sos_id):

    sos_request = SOSRequest.query.get(sos_id)

    if not sos_request:
        return jsonify({
            "status": "error",
            "message": "SOS request not found"
        }), 404

    data = request.get_json()

    sos_request.status = data.get("status", sos_request.status)
    sos_request.priority = data.get("priority", sos_request.priority)

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "SOS updated successfully"
    })
# Delete SOS
@sos.route("/delete/<int:sos_id>", methods=["DELETE"])
@role_required("Admin")
def delete_sos(sos_id):

    sos_request = SOSRequest.query.get(sos_id)

    if not sos_request:
        return jsonify({
            "status": "error",
            "message": "SOS request not found"
        }), 404

    db.session.delete(sos_request)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "SOS deleted successfully"
    }), 200