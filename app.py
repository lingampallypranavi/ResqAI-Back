import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask
from config import Config
from extensions import db

from models.user import User
from models.sos import SOSRequest

from routes.auth import auth
from routes.sos import sos
from flask_jwt_extended import JWTManager
from models.shelter import Shelter
from routes.shelter import shelter
from models.rescue import RescueTeam
from routes.rescue import rescue
from routes.admin import admin

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(sos, url_prefix="/sos")
app.register_blueprint(shelter, url_prefix="/shelter")
app.register_blueprint(
    rescue,
    url_prefix="/rescue"
)
app.register_blueprint(admin, url_prefix="/admin")

@app.route("/")
def home():
    return "🚀 ResQAI Backend is Running Successfully!"


if __name__ == "__main__":
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Done!")

    app.run(debug=True)