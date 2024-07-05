import datetime, time
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from enum import Enum
from fastapi_users import FastAPIUsers, fastapi_users

from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.database import User
from auth.schemas import UserCreate, UserRead

app = FastAPI(
    title="Trading App"
)

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)




# fake_users = [{"id": 1, "role": "admin", "name": "John", "degree":[{"id":1, "created_at": "2020-01-01", "type_degree": "newbie"}] }, {"id": 2, "role": "user", "name": "Jane", "degree":[{"id":1, "created_at": "2020-01-01", "type_degree": "newbie"}]}]

# class DegreeType(Enum):
#     newbie = "newbie"
#     expert = "expert"

# class Degree(BaseModel):
#     id:int
#     created_at: datetime
#     type_degree:DegreeType

#     class Config:
#         arbitrary_types_allowed = True

# class User(BaseModel):
#     id:int
#     role:str
#     name:str
#     degree: Optional[list[Degree]]
#  @app.get("/users/{user_id}", response_model=List[User])
# def hello(user_id: int):
#     return [user for user in fake_users if user.get("id") == user_id]


# fake_trades = [
#     {"id":1, "user_id":1, "current": "BTC", "side": "buy", "price": 10000, "amount": 2.12},
#     {"id":2, "user_id":1, "current": "BTC", "side": "sell", "price": 10003, "amount": 2.12},
# ]


# @app.get("/trades")
# def get_trades(limit: int=1, offset: int=0):
#     return fake_trades[offset:][:limit]

# @app.post("/users/{user_    id}")
# def change_user_name(user_id:int, new_name:str):
#     current_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
#     current_user["name"] = new_name
#     return {"status": "ok", "data": current_user}

# class Trade(BaseModel):
#     id:int 
#     user_id:int
#     current:str
#     side:str
#     price:float =Field(ge=0)
#     amount:float

# @app.post("/trades")
# def add_trades(trades:List[Trade]):
#     fake_trades.extend(trades)
#     return {"status": "ok", "data": fake_trades}
