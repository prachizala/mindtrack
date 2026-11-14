# Technical Interview Questions & Answers — MindTrack

Based on the actual codebase in `mindtrack`.

---

### Question 1: How does AES-256 field-level encryption work in `encryption.py`?
**Answer:**
In `app/core/encryption.py`, journaling privacy is protected using Python's `cryptography.fernet.Fernet`:
1. **Underlying Cipher:** Fernet implements AES in CBC mode with a 128-bit key for encryption and PKCS7 padding, combined with HMAC-SHA256 using another 128-bit key for authentication and integrity. Together, this represents a 256-bit symmetric key scheme.
2. **Key Derivation Fallback:** A standard Fernet cipher strictly requires a 32-byte URL-safe base64-encoded key. If an administrator passes an arbitrary passphrase, a naive initialization throws `ValueError`. To solve this, `get_fernet_cipher()` catches the error and derives a cryptographic key via SHA-256:
   ```python
   derived = base64.urlsafe_b64encode(hashlib.sha256(key_str.encode("utf-8")).digest())
   return Fernet(derived)
   ```
3. **Database Isolation:** When a user logs an entry, `encrypt_journal_text(plain_text)` returns ciphertext bytes decoded to a base64 string. The database column `JournalEntry.encrypted_content` stores only this ciphertext. Decryption happens strictly in-memory during authorized user retrieval.

---

### Question 2: How does the offline crisis detection sentinel work in `safety_sentinel.py`?
**Answer:**
In `app/services/safety_sentinel.py`, user safety is enforced deterministically:
1. **Pre-Storage Scanning:** Before the journal entry is encrypted and persisted, `evaluate_distress_signals(text, polarity)` inspects the plaintext.
2. **Regex Patterns:** The text is scanned against compiled regex expressions for explicit self-harm signals (e.g., `suicid`, `kill myself`, `end my life`, `want to die`, `no reason to live`, `self harm`, etc.).
3. **Polarity Threshold:** If distress keywords match, or if the sentiment polarity score is $\le -0.60$, the system flags `distress_detected: True`.
4. **Helpline Routing:** The API immediately attaches emergency support metadata to the response:
   - **Tele-MANAS:** 14416 / 1800-891-4416 (24/7 Toll-Free National Mental Health Helpline, Government of India)
   - **Vandrevala Foundation:** +91 9999 666 555 (24/7 Free Psychological Support)
   - **KIRAN:** 1800-599-0019 (24/7 Government Distress Support)
   - Non-medical disclaimer clearly stating that MindTrack is a self-reflection tool, not clinical intervention.

---

### Question 3: Why use an offline regex sentinel instead of an external LLM for crisis detection?
**Answer:**
1. **Zero Latency:** Regex evaluation completes in less than 1 millisecond on CPU, whereas LLM network calls take 1–3 seconds.
2. **Determinism:** Regex pattern matching never suffers from prompt injection, token exhaustion, network outages, or probabilistic refusal.
3. **Privacy:** The user's unencrypted text never leaves the application process boundary or crosses an external API.

---

### Question 4: What hard bug did you fix in `mindtrack` during stabilization?
**Answer:**
**The Bug:** During local container setup, when `ENCRYPTION_MASTER_KEY` was set to a simple alphanumeric string (e.g., `my_secret_key_12345`), the application crashed on startup with `binascii.Error: Incorrect padding` or `ValueError: Fernet key must be 32 url-safe base64-encoded bytes`.  
**The Solution:** I implemented the deterministic SHA-256 derivation fallback in `get_fernet_cipher()`. If direct initialization fails, the passphrase is automatically passed through `hashlib.sha256()` to yield exactly 32 bytes of uniform entropy and encoded with `base64.urlsafe_b64encode()`. This made deployment configuration completely resilient.
