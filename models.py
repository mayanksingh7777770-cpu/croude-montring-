
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from core.database import Base
from datetime import datetime

class Camera(Base):
    __tablename__ = "cameras"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    rtsp_url = Column(String)
    ticket_price = Column(Float, default=0.0)

class EntryLog(Base):
    __tablename__ = "entry_logs"
    id = Column(Integer, primary_key=True, index=True)
    camera_id = Column(Integer, ForeignKey("cameras.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    tracking_id = Column(Integer)
    face_name = Column(String, nullable=True)
    direction = Column(String)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    face_encoding = Column(String)
