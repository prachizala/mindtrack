# Product Requirements Document (PRD)
## MindTrack: Privacy-First Journal & Wellness Companion

### 1. Executive Summary & Problem Statement
Daily emotional journaling delivers established therapeutic benefits for anxiety and stress management. However, users frequently avoid logging raw thoughts in cloud-based wellness applications due to profound fears of data exposure, employer scrutiny, or advertising profiling. Simultaneously, many unregulated AI mental health apps inappropriately generate pseudo-clinical diagnoses without critical safety nets during acute crisis episodes.

**MindTrack** delivers a **privacy-first, client-encrypted wellness journaling application**. Journal bodies are locally encrypted with AES-256 before disk persistence. The platform incorporates automated sentiment and mood trajectory analysis, generating gentle weekly reflective summaries. Most critically, MindTrack embeds a deterministic **Safety Sentinel**: displaying an uncompromising non-medical disclaimer and surfacing verified emergency crisis resources whenever strong distress signals are detected.

---

### 2. User Personas
- **Student / Young Professional**: Experiences academic or workplace burnout and seeks an uncompromised, confidential space for daily emotional reflection.
- **Mindfulness Practitioner**: Tracks mood fluctuations, identifying correlations between sleep, exercise, and subjective emotional well-being.
- **Safety Conscious Individual**: Demands mathematical guarantees that personal journal text cannot be read by server administrators or third parties.

---

### 3. Scope & Prioritization (MoSCoW)
Scope is strictly frozen at the conclusion of Day 1.

#### MUST HAVE (Target MVP - Days 1-5)
- **Daily Mood & Emotion Logging**: 1-10 numerical scale paired with granular emotion category tags (e.g., Grateful, Anxious, Calm, Exhausted, Hopeful).
- **Free-Form Journal with Local AES-256 Encryption**: Journal text bodies encrypted with Fernet (AES-128-CBC / AES-256 equivalent) using a user-held encryption key; database stores only ciphertext.
- **Sentiment & Emotional Polarity Engine**: Automated analysis calculating polarity (-1.0 to +1.0), subjectivity, and emotional spectrum markers without leaking unencrypted text.
- **Longitudinal Trend Analytics**: 7-day and 30-day interactive mood and sentiment trajectory graphs powered by Recharts.
- **Weekly AI Gentle Reflection**: Structured, empathetic summary highlighting cognitive wins, emotional trends, and mindful journaling prompts.
- **MANDATORY SAFETY SENTINEL & DISCLAIMER (NON-NEGOTIABLE)**:
  - **Prominent Non-Medical Notice**: Fixed persistent banner: *"MindTrack is an emotional well-being reflection tool, not a clinical healthcare service. It does not provide medical diagnosis, treatment, or psychiatric care."*
  - **Deterministic Crisis Sentinel**: Hardened keyword pattern matcher & extreme negative sentiment detector that instantly displays a supportive **Crisis Assistance Modal** with verified 24/7 toll-free hotlines (India: Tele-MANAS 14416 / 1800-891-4416, Vandrevala Foundation +91 9999 666 555, KIRAN 1800-599-0019; International: 988 Suicide & Crisis Lifeline).

#### SHOULD HAVE (Days 5-6)
- Encrypted export of personal journal archive (JSON backup).
- Mindful breathing pacer widget.

#### COULD HAVE (Deferred to Post-MVP)
- Offline-first PWA caching with IndexedDB.
- Voice-to-text note capture via local Whisper model.

#### WON'T HAVE (Out of Scope for 7-Day Sprint)
- Clinical therapist telehealth appointments or chat.
- Medication tracking or prescription logs.

---

### 4. Non-Functional Requirements
- **Privacy Assurance**: Zero unencrypted journal text in database files, access logs, or error stack traces.
- **Safety Reliability**: Distress sentinel runs deterministically on input BEFORE any LLM invocation and operates even when offline.
- **Zero-Judgment UX**: Tone is empathetic, supportive, and non-prescriptive.
