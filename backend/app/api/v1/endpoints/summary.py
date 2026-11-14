from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.core.encryption import decrypt_journal_text
from app.models.models import User, JournalEntry
from app.services.summary_service import generate_weekly_reflection

router = APIRouter()

@router.get("/weekly")
def get_weekly(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    entries = db.query(JournalEntry).filter(JournalEntry.user_id == current_user.id).all()
    e_dicts = [{"mood_score": e.mood_score, "emotion_tags": e.emotion_tags} for e in entries]
    reflection = generate_weekly_reflection(e_dicts)
    return {"reflection": reflection}
