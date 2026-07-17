from extensions import db
from datetime import datetime


class RescueTeam(db.Model):

    __tablename__ = "rescue_teams"

    rescue_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    team_name = db.Column(
        db.String(100),
        nullable=False
    )

    location = db.Column(
        db.String(255),
        nullable=False
    )

    contact = db.Column(
        db.String(15),
        nullable=False
    )

    # Team availability
    status = db.Column(
        db.String(50),
        default="Available"
    )

    # Assigned SOS Request
    assigned_sos_id = db.Column(
        db.Integer,
        db.ForeignKey("sos_requests.sos_id"),
        nullable=True
    )

    # Rescue progress
    rescue_status = db.Column(
        db.String(50),
        default="Available"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )