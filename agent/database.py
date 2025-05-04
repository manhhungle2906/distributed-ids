from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database file path
DATABASE_URL = "sqlite:///logs.db"

# Create engine and session
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)  # 🔥 ĐÂY LÀ DÒNG GÂY LỖI NẾU THIẾU

# Define base
Base = declarative_base()

# Table definition
class SystemLog(Base):
    __tablename__ = "system_logs"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String(255))
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    processes = Column(Text)  # JSON string
    timestamp = Column(DateTime, default=datetime.utcnow)
