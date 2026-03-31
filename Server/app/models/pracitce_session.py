# Practice Session Model

from sqlalchemy import Column, BigInteger, String, Integer, DateTime
from database import Base

class PracticeSession(Base):
    __tablename__ = 'practice_sessions'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    session_name = Column(String(100), nullable=False)
    audio_file = Column(Text, nullable=True)  # Replaced notes and activity_type with audio_file
    user_id = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default="2026-03-31 02:01:17")  # Current Date and Time

    def __repr__(self):
        return f'<PracticeSession(id={self.id}, session_name={self.session_name}, audio_file={self.audio_file}, user_id={self.user_id}, timestamp={self.timestamp})>'