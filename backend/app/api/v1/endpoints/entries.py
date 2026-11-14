from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from app.core.database import get_db
from app.core.security import get_current_user
from app.core.encryption import encrypt_journal_text, decrypt_journal_text
from app.models.models import User, JournalEntry
from app.services.sentiment_service import analyze_sentiment
from app.services.safety_sentinel import evaluate_distress_signals

router = APIRouter()

class CreateEntryRequest(BaseModel):
    entry_date: str
    mood_score: int
    emotion_tags: str
    journal_text: str

@router.post("/")
def create_entry(req: CreateEntryRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # 1. Sentiment analysis on raw text in-memory
    sentiment = analyze_sentiment(req.journal_text)

    # 2. Safety sentinel inspection
    safety = evaluate_distress_signals(req.journal_text, sentiment["polarity"])

    # 3. Encrypt journal body before saving to DB
    encrypted_body = encrypt_journal_text(req.journal_text)

    entry = JournalEntry(
        user_id=current_user.id,
        entry_date=req.entry_date,
        mood_score=req.mood_score,
        emotion_tags=req.emotion_tags,
        encrypted_body=encrypted_body,
        sentiment_polarity=sentiment["polarity"],
        sentiment_subjectivity=sentiment["subjectivity"],
        distress_flag_triggered=safety["distress_detected"]
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)

    return {
        "id": entry.id,
        "entry_date": entry.entry_date,
        "mood_score": entry.mood_score,
        "sentiment": sentiment,
        "safety_alert": safety if safety["distress_detected"] else None,
        "message": "Journal entry encrypted with AES-256 and saved."
    }

@router.get("/")
def list_entries(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    entries = db.query(JournalEntry).filter(JournalEntry.user_id == current_user.id).order_by(JournalEntry.entry_date.desc()).all()
    out = []
    for e in entries:
        out.append({
            "id": e.id,
            "entry_date": e.entry_date,
            "mood_score": e.mood_score,
            "emotion_tags": e.emotion_tags,
            "decrypted_body": decrypt_journal_text(e.encrypted_body),
            "sentiment_polarity": e.sentiment_polarity,
            "distress_flag": e.distress_flag_triggered
        })
    return out

@router.get("/export/encrypted")
def export_encrypted_backup(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    entries = db.query(JournalEntry).filter(JournalEntry.user_id == current_user.id).all()
    return {
        "user_email": current_user.email,
        "total_entries": len(entries),
        "cipher_records": [{
            "date": e.entry_date,
            "mood": e.mood_score,
            "encrypted_payload": e.encrypted_body
        } for e in entries]
    }
