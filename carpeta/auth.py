from passlib.context import CryptContext
from passlib.hash import argon2
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecreto123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")


# HASH PASSWORD
def hash_password(password: str):
    return argon2.hash(password)


def verify_password(plain, hashed):
    return argon2.verify(plain, hashed)


# TOKEN
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
