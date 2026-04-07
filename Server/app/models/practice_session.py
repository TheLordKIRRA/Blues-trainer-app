from app.db.database import db
from datetime import datetime

class PracticeSession(db.Model):
    __tablename__ = "practice_sessions"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    session_name = db.Column(db.VARCHAR(100), nullable=False)
    audio_file = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref="practice_sessions")

    def to_dict(self):
        return {
            "id": self.id,
            "session_name": self.session_name,
            "audio_file": self.audio_file,
            "user_id": self.user_id,
            "timestamp": self.timestamp.isoformat()
        }
