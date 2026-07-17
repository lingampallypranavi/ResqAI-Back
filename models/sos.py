from extensions import db
from datetime import datetime

class SOSRequest(db.Model):
    __tablename__ = "sos_requests"

    sos_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    disaster_type = db.Column(db.String(100), nullable=False)

    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    priority = db.Column(db.String(20), default="Medium")

    status = db.Column(db.String(20), default="Pending")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)