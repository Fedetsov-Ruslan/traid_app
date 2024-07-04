from typing import Optional
from fastapi_users import schemas

class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    user_name: str
    is_active: Optional[bool] = True
    is_siperuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config():
        orm_mode = True
        
class UserCreate(schemas.BaseUserCreate):
    user_name: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_siperuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass