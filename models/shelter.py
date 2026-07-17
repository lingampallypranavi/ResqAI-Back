from extensions import db
from datetime import datetime


class Shelter(db.Model):
    __tablename__ = "shelters"

    shelter_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    location = db.Column(db.String(255), nullable=False)

    capacity = db.Column(db.Integer, nullable=False)

    available_capacity = db.Column(db.Integer, nullable=False)

    contact = db.Column(db.String(15), nullable=False)

    created_at = db.Column(
    db.DateTime,
    default=datetime.utcnow,
    nullable=False
)