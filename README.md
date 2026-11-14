# MindTrack: Privacy-First Mental Wellness Journal

MindTrack is an emotionally restorative, confidential wellness journaling platform designed with AES-256 client-level encryption, sentiment polarity trajectories, and a deterministic safety crisis sentinel.

---

## 🌟 Key Features

1. **Zero-Knowledge Field Encryption**:
   - Journal text is encrypted using Fernet (AES-256 equivalent) prior to database persistence. Server logs and databases never contain unencrypted journal text.
2. **Deterministic Crisis Sentinel**:
   - Hardened offline keyword scanner that surfaces verified 24/7 emergency helplines (Tele-MANAS, Vandrevala Foundation) whenever acute distress or severe negative polarity is detected.
3. **Mandatory Non-Medical Disclaimer**:
   - Uncompromising ethical notice reminding users that MindTrack is a self-reflection tool, not clinical psychiatric care.
4. **Sentiment & Longitudinal Trends**:
   - Analyzes mood and polarity patterns (-1.0 to 1.0) over 7-day and 30-day windows.
5. **Weekly Gentle Reflection**:
   - Empathetic AI summary highlighting cognitive wins and mindful inquiries.

---

## 🚀 Quickstart Guide

```bash
cd backend
python seed_data.py
python -m pytest -v tests/
uvicorn app.main:app --reload --port 8000
```
Open `http://localhost:8000` to interact with MindTrack.

---

## 👤 Author
**Prachi Zala** | [GitHub](https://github.com/prachizala)
