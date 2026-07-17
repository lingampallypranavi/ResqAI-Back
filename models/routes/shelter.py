from flask import Blueprint, request, jsonify
from extensions import db
from models.shelter import Shelter
from flask_jwt_extended import jwt_required
from utils.roles import role_required

shelter = Blueprint("shelter", __name__)


# Test API
@shelter.route("/test", methods=["GET"])
def test():
    return jsonify({
        "status": "success",
        "message": "Shelter API is Working!"
    })


# Create Shelter (Admin only)
@shelter.route("/create", methods=["POST"])
@role_required("Admin")
def create_shelter():

    data = request.get_json()

    new_shelter = Shelter(
        name=data["name"],
        location=data["location"],
        capacity=data["capacity"],
        available_capacity=data["available_capacity"],
        contact=data["contact"]
    )

    db.session.add(new_shelter)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Shelter created successfully",
        "shelter_id": new_shelter.shelter_id
    }), 201


# Get All Shelters
@shelter.route("/all", methods=["GET"])
@jwt_required()
def get_all_shelters():

    shelters = Shelter.query.all()

    result = []

    for s in shelters:
        result.append({
            "shelter_id": s.shelter_id,
            "name": s.name,
            "location": s.location,
            "capacity": s.capacity,
            "available_capacity": s.available_capacity,
            "contact": s.contact,
            "created_at": s.created_at.strftime("%Y-%m-%d %H:%M:%S")
        })

    return jsonify({
        "status": "success",
        "count": len(result),
        "data": result
    })


# Get Shelter by ID
@shelter.route("/<int:shelter_id>", methods=["GET"])
@jwt_required()
def get_shelter(shelter_id):

    s = Shelter.query.get(shelter_id)

    if not s:
        return jsonify({
            "status": "error",
            "message": "Shelter not found"
        }), 404

    return jsonify({
        "status": "success",
        "data": {
            "shelter_id": s.shelter_id,
            "name": s.name,
            "location": s.location,
            "capacity": s.capacity,
            "available_capacity": s.available_capacity,
            "contact": s.contact,
            "created_at": s.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
    })


# Update Shelter (Admin only)
@shelter.route("/update/<int:shelter_id>", methods=["PUT"])
@role_required("Admin")
def update_shelter(shelter_id):

    shelter_data = Shelter.query.get(shelter_id)

    if not shelter_data:
        return jsonify({
            "status": "error",
            "message": "Shelter not found"
        }), 404

    data = request.get_json()

    shelter_data.name = data.get("name", shelter_data.name)
    shelter_data.location = data.get("location", shelter_data.location)
    shelter_data.capacity = data.get("capacity", shelter_data.capacity)
    shelter_data.available_capacity = data.get(
        "available_capacity",
        shelter_data.available_capacity
    )
    shelter_data.contact = data.get("contact", shelter_data.contact)

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Shelter updated successfully"
    })


# Delete Shelter (Admin only)
@shelter.route("/delete/<int:shelter_id>", methods=["DELETE"])
@role_required("Admin")
def delete_shelter(shelter_id):

    shelter_data = Shelter.query.get(shelter_id)

    if not shelter_data:
        return jsonify({
            "status": "error",
            "message": "Shelter not found"
        }), 404

    db.session.delete(shelter_data)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Shelter deleted successfully"
    })