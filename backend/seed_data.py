from app.core.database import SessionLocal, Base, engine
from app.core.security import hash_password
from app.core.encryption import encrypt_journal_text
from app.models.models import User, JournalEntry

Base.metadata.create_all(bind=engine)
db = SessionLocal()

print("Seeding MindTrack database...")

user = db.query(User).filter(User.email == "prachi@mindtrack.app").first()
if not user:
    user = User(
        email="prachi@mindtrack.app",
        hashed_password=hash_password("mindtrack123"),
        full_name="Prachi Zala"
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    entries_data = [
        ("2026-11-05", 8, "Grateful, Focused, Energized", "Started the 7-day multi-agent sprint today. Felt organized and motivated by the architecture plan.", 0.60, False),
        ("2026-11-07", 7, "Calm, Productive", "Completed the database schemas and auth tokens. Everything tested cleanly.", 0.40, False),
        ("2026-11-09", 5, "Tired, Stressed", "Felt overwhelmed by concurrent project tests, but took a walk and refocused.", -0.20, False),
        ("2026-11-11", 8, "Accomplished, Hopeful", "Landed the core RAG and face recognition biometrics. Momentum is high.", 0.70, False),
        ("2026-11-13", 9, "Grateful, Peaceful", "All four projects passing test suites. Feeling deeply proud of the engineering work.", 0.85, False)
    ]

    for date, mood, tags, body, pol, dist in entries_data:
        e = JournalEntry(
            user_id=user.id,
            entry_date=date,
            mood_score=mood,
            emotion_tags=tags,
            encrypted_body=encrypt_journal_text(body),
            sentiment_polarity=pol,
            sentiment_subjectivity=0.45,
            distress_flag_triggered=dist
        )
        db.add(e)
    db.commit()

print("MindTrack database seeded successfully!")
