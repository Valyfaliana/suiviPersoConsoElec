from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()  # paramètres sûrs par défaut

# Hasher (lors de l'inscription)
def hash_password(plain_password: str) -> str:
    return ph.hash(plain_password)

# Vérifier (lors du login)
def verify_password(stored_hash: str, provided_password: str) -> bool:
    try:
        return ph.verify(stored_hash, provided_password)
    except VerifyMismatchError:
        return False
