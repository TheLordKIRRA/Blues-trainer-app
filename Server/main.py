from flask import Flask
from flask_cors import CORS
from app.db.database import init_db, db
from app.api.auth_routes import auth_bp
from app.api.practice_routes import practice_bp

def create_app():
  app = Flask(__name__)
  CORS(app)

  app.config["SQALCHEMY_DATABASE_URI"] = "root:1234@db:127.0.0.1/blues_trainer_app"
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.config["SECRET_KEY"] = "supersecretkey"

  init_db(app)

  app.register_blueprint(auth_bp, url_prefix="/api/auth")
  app.register_blueprint(practice_bp, url_prefix="/api/practice")

  return app

app = create_app()

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
