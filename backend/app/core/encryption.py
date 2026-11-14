import base64
import hashlib
from cryptography.fernet import Fernet
from app.core.config import settings

def get_fernet_cipher() -> Fernet:
    key_str = settings.ENCRYPTION_MASTER_KEY
    try:
        # Try direct initialization if already a valid 32-byte urlsafe base64 key
        return Fernet(key_str.encode("utf-8"))
    except Exception:
        # Robust derivation: sha256 hash of secret key -> base64
        derived = base64.urlsafe_b64encode(hashlib.sha256(key_str.encode("utf-8")).digest())
        return Fernet(derived)

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
