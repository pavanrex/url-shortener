from sqlalchemy import Column, Integer, String
from app.db.database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_id = Column(String, unique=True, index=True)
    long_url = Column(String)