from passlib.context import CryptContext

pwt_cxt  = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwt_cxt.hash(password)

    def verify(hashed_password, plain_password):
        return pwt_cxt.verify(plain_password, hashed_password)