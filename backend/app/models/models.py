from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    entries = relationship("JournalEntry", back_populates="user")
    summaries = relationship("WeeklySummary", back_populates="user")

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    entry_date = Column(String, nullable=False)  # YYYY-MM-DD
    mood_score = Column(Integer, nullable=False)  # 1 to 10
    emotion_tags = Column(String, default="")  # comma separated
    encrypted_body = Column(Text, nullable=False)  # AES-256 ciphertext
    sentiment_polarity = Column(Float, default=0.0)  # -1.0 to 1.0
    sentiment_subjectivity = Column(Float, default=0.5)
    distress_flag_triggered = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="entries")

class WeeklySummary(Base):
    __tablename__ = "weekly_summaries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    week_start = Column(String, nullable=False)
    average_mood = Column(Float, default=7.0)
    summary_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="summaries")
