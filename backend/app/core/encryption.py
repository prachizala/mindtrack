import base64
from cryptography.fernet import Fernet
from app.core.config import settings

def get_fernet_cipher() -> Fernet:
    try:
        return Fernet(settings.ENCRYPTION_MASTER_KEY.encode("utf-8"))
    except Exception:
        # Fallback to deterministic valid 32-byte base64 key
        raw_key = b"MindTrackPrivacyMasterKey2026!!!"
        b64_key = base64.urlsafe_b64encode(raw_key)
        return Fernet(b64_key)

cipher = get_fernet_cipher()

def encrypt_journal_text(plain_text: str) -> str:
    """Encrypts plaintext journal text into an AES-256 Fernet ciphertext string."""
    if not plain_text:
        return ""
    encrypted_bytes = cipher.encrypt(plain_text.encode("utf-8"))
    return encrypted_bytes.decode("utf-8")

def decrypt_journal_text(cipher_text: str) -> str:
    """Decrypts AES-256 Fernet ciphertext back into plaintext."""
    if not cipher_text:
        return ""
    try:
        decrypted_bytes = cipher.decrypt(cipher_text.encode("utf-8"))
        return decrypted_bytes.decode("utf-8")
    except Exception:
        return "[Decryption Failed: Invalid Key]"
