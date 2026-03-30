from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes=['pbkdf2_sha256'],deprecated='auto')

class Hash:
    @staticmethod
    def hash(password:str):
        return pwd_cxt.hash(password)
    
    @staticmethod
    def verify(plain_pass:str,hashed_pass:str):
        return pwd_cxt.verify(plain_pass,hashed_pass)
