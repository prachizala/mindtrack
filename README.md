# MindTrack: Privacy-First Mental Wellness Journal (API Prototype)

> **Note:** This backend prototype has been integrated and superseded by our full-stack Streamlit NLP suite [MindPulse: Mood Tracker & Sentiment Analysis](https://github.com/prachizala/mood-tracker-sentiment-analysis). Kept here as an API reference.

[![MindTrack CI](https://github.com/prachizala/mindtrack/actions/workflows/ci.yml/badge.svg)](https://github.com/prachizala/mindtrack/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

MindTrack is an emotionally restorative, confidential wellness journaling platform designed with zero-knowledge AES-256 field-level encryption, sentiment polarity trajectories, and a deterministic safety crisis sentinel.

---

## Key Features

1. **Zero-Knowledge Field Encryption**:
   - Journal entries are encrypted using Fernet (AES-128-CBC / HMAC-SHA256 authenticated symmetric encryption) before SQLite database persistence. Server logs and databases never contain raw unencrypted journal text.
2. **Deterministic Crisis Sentinel**:
   - Offline keyword scanner and rule-based detector that immediately surfaces verified 24/7 emergency helplines (Tele-MANAS, Vandrevala Foundation) whenever acute distress or severe negative polarity is detected.
3. **Mandatory Non-Medical Disclaimer**:
   - Ethical safeguards explicitly clarifying that MindTrack is a self-reflection tool, not clinical psychiatric intervention.
4. **Sentiment & Longitudinal Trends**:
   - Computes mood and polarity patterns (-1.0 to 1.0) over 7-day and 30-day temporal windows.
5. **Weekly Gentle Reflection**:
   - Empathetic AI summary highlighting cognitive wins, mood shifts, and mindful prompts.

---

## API Endpoints Table

Base URL: `http://localhost:8000`

| Method | Endpoint | Description | Auth Required |
|:---|:---|:---|:---:|
| `GET` | `/api/health` | Health check and service metadata | No |
| `POST` | `/api/v1/seed` | Seed realistic demo journal entries & users | No |
| `POST` | `/api/v1/auth/register` | Register a new user | No |
| `POST` | `/api/v1/auth/login` | Authenticate and obtain JWT bearer token | No |
| `GET` | `/api/v1/entries/` | Retrieve user's decrypted journal entries | Bearer Token |
| `POST` | `/api/v1/entries/` | Create a new encrypted journal entry | Bearer Token |
| `GET` | `/api/v1/analytics/trends` | Compute sentiment & mood trends over time | Bearer Token |
| `GET` | `/api/v1/summary/weekly` | Generate weekly reflection summary | Bearer Token |
| `GET` | `/api/v1/safety/resources` | Fetch verified crisis helpline resources | No |

---

## Quickstart Guide

### 1. Environment Setup
```bash
cd mindtrack
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install --upgrade pip
pip install -r backend/requirements.txt
```

### 2. Populate Demo Data
```bash
python backend/seed_data.py
```

### 3. Run Server
```bash
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```
Open `http://localhost:8000` to interact with MindTrack, or `http://localhost:8000/docs` for Swagger UI.

### 4. Run Pytest Suite
```bash
pytest backend/tests/test_mindtrack.py -v
```

---

## Repository Status & Flagship Supersession
This repository is retained as an architectural API prototype. For the actively maintained full-stack data analytics and sentiment analysis suite featuring Streamlit, HuggingFace Transformers, and longitudinal visualization, please see:
👉 **[MindPulse: Mood Tracker & Sentiment Analysis](https://github.com/prachizala/mood-tracker-sentiment-analysis)**

---

## Author & License
- **Author:** Prachi Zala ([prachizala](https://github.com/prachizala))
- **Email:** prachizala2003@gmail.com
- **License:** MIT License. See [LICENSE](LICENSE) for details.
