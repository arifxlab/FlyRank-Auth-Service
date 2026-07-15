from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.schemas.auth import (
    RegisterRequest,
)


class AuthService:

    @staticmethod
    def register(
        db: Session,
        data: RegisterRequest,
    ) -> User:

        existing_user = (
            db.query(User)
            .filter(User.email == data.email)
            .first()
        )

        if existing_user:
            raise ValueError("Email already registered")

        user = User(
            email=data.email,
            hashed_password=hash_password(data.password),
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def login(
            db: Session,
            email: str,
            password: str,
    ):

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise ValueError("Invalid email or password")

        return create_access_token(
            subject=user.email
        )