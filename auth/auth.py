from fastapi_users.authentication import AuthenticationBackend, CookieTransport
from fastapi_users.authentication import JWTStrategy
from config import SECRET_KEY

cockie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)

SECRET = SECRET_KEY

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cockie_transport,
    get_strategy=get_jwt_strategy,
)