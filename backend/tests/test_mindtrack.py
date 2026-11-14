import pytest
from app.core.encryption import encrypt_journal_text, decrypt_journal_text
from app.services.safety_sentinel import evaluate_distress_signals, NON_MEDICAL_DISCLAIMER
from app.services.sentiment_service import analyze_sentiment

def test_aes_journal_encryption():
    plain = "Personal private thoughts: Today I felt deeply reflective and calm."
    cipher = encrypt_journal_text(plain)

    # Must be encrypted: cipher should NOT equal plain and should not contain words from plain
    assert cipher != plain
    assert "reflective" not in cipher
    assert "private" not in cipher

    # Decrypt restores original
    restored = decrypt_journal_text(cipher)
    assert restored == plain

def test_deterministic_crisis_sentinel_detection():
    # Normal reflective text
    normal = evaluate_distress_signals("Had a productive study day and reviewed data structures.", polarity=0.4)
    assert normal["distress_detected"] is False
    assert len(normal["helplines"]) == 0

    # Acute crisis phrase triggers sentinel
    crisis = evaluate_distress_signals("Feeling like I want to end my life, everything is hopeless.", polarity=-0.8)
    assert crisis["distress_detected"] is True
    assert len(crisis["helplines"]) > 0
    assert "Tele-MANAS" in crisis["helplines"][0]["name"]
    assert NON_MEDICAL_DISCLAIMER in crisis["non_medical_disclaimer"]

def test_sentiment_analysis():
    pos = analyze_sentiment("I feel so happy, grateful, and accomplished today!")
    assert pos["polarity"] > 0.4

    neg = analyze_sentiment("I feel sad, anxious, and deeply overwhelmed.")
    assert neg["polarity"] < -0.3


def test_key_derivation_resilience():
    # Verify that raw secret string is safely derived into valid 32-byte key
    import hashlib, base64
    from cryptography.fernet import Fernet
    raw = "MyArbitraryPassphrase123!"
    derived = base64.urlsafe_b64encode(hashlib.sha256(raw.encode()).digest())
    f = Fernet(derived)
    token = f.encrypt(b"Test message")
    assert f.decrypt(token) == b"Test message"
