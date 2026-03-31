from app.db.database import db
from datetime import datetime

class PracticeSession(db.Model):
    __tablename__ = "practice_sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(500))
    activity_type = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref="practice_sessions")

    def to_dict(self):
        return {
            "id": self.id,
            "duration_minutes": self.duration_minutes,
            "notes": self.notes,
            "activity_type": self.activity_type,
            "timestamp": self.timestamp.isoformat()
        }
