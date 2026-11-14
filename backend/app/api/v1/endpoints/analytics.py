from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.models import User, JournalEntry

router = APIRouter()

@router.get("/trends")
def get_trends(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    entries = db.query(JournalEntry).filter(JournalEntry.user_id == current_user.id).order_by(JournalEntry.entry_date.asc()).limit(14).all()
    trends = []
    for e in entries:
        trends.append({
            "date": e.entry_date,
            "mood": e.mood_score,
            "polarity": e.sentiment_polarity,
            "tags": e.emotion_tags
        })
    return {"trends": trends}
