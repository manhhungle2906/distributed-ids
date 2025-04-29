from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json

DATABASE_URL = "sqlite:///logs.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class SystemLog(Base):
    __tablename__ = "system_logs"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String(255))
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    processes = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

def save_log(data):
    db = SessionLocal()
    try:
        log_entry = SystemLog(
            hostname=data.get("hostname"),
            cpu_usage=data.get("cpu_usage"),
            memory_usage=data.get("memory_usage"),
            processes=json.dumps(data.get("processes", []))
        )
        db.add(log_entry)
        db.commit()
        print(f"[DB] Log saved for {data.get('hostname')}")
    except Exception as e:
        print(f"[DB] Error saving log: {e}")
        db.rollback()
    finally:
        db.close()
