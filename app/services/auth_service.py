import os
from datetime import datetime, timedelta, timezone

import bcrypt
from dotenv import load_dotenv
from jose import jwt
from sqlalchemy.orm import Session

from app.models.user import User

load_dotenv(dotenv_path=".env")


JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRE_MINUTES = int(
    os.getenv("JWT_EXPIRE_MINUTES", "60")
)


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")

    password_hash = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt(),
    )

    return password_hash.decode("utf-8")


def verify_password(
    plain_password: str,
    password_hash: str,
) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        password_hash.encode("utf-8"),
    )


def get_user_by_email(
    db: Session,
    email: str,
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def create_user(
    db: Session,
    email: str,
    password: str,
):
    password_hash = hash_password(password)

    user = User(
        email=email,
        password_hash=password_hash,
        role="USER",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def create_access_token(
    user_id: int,
    email: str,
) -> str:

    if not JWT_SECRET:
        raise RuntimeError(
            "JWT_SECRET is not configured."
        )

    now = datetime.now(timezone.utc)

    expires_at = (
        now
        + timedelta(minutes=JWT_EXPIRE_MINUTES)
    )

    payload = {
        "sub": str(user_id),
        "email": email,
        "iat": now,
        "exp": expires_at,
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM,
    )
