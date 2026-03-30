from sqlalchemy import Column, Integer, String, DateTime
from app.db.database import Base
from datetime import datetime

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_id = Column(String, unique=True, index=True)
    long_url = Column(String)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)