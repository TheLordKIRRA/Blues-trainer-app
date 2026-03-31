from pydantic import BaseModel
from typing import Optional

class PracticeMetricsData(BaseModel):
    id: Optional[int] = None  # bigint UN AI PK (auto-increment, unsigned)
    Tone: str  # varchar(100)
    Pitch: str  # varchar(100)
    Tempo: str  # varchar(100)
    Accuracy: str  # varchar(100)
    Overall: str  # varchar(100)

    class Config:
        from_attributes = True
