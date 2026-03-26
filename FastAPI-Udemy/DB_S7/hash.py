from passlib.context import CryptContext

# Use PBKDF2 instead of bcrypt
pwd_cxt = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

class Hash:
    @staticmethod
    def hash(password: str):
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(password: str, hashed_pass: str):
        return pwd_cxt.verify(password, hashed_pass)