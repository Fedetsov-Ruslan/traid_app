import uuid
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, UUIDIDMixin

from database import get_user_db, User
from config import SECRET_KEY

SECRET = SECRET_KEY

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Request | None = None) -> None:
        return await super().on_after_register(user, request)
    
    async def on_after_forgot_password(
        self, user: User, token: str, request: Request | None = None
    ) -> None:
        return await super().on_after_forgot_password(user, token, request)
    
    async def on_after_request_verify(
        self, user: User, token: str, request: Request | None = None
    ) -> None:
        return await super().on_after_request_verify(user, token, request)
    
    async def get_user_manager(user_db=Depends(get_user_db)):
        yield UserManager(user_db)

