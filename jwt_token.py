from fastapi import HTTPException, Header, Depends
import jwt
import datetime
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "d1d88dfc56771f84c62e557a397ff3b4dde5fda1d5fbd42fb3d7a5955a451fb9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

security = HTTPBearer()


def get_authorization_header(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    return token


def verify_token(token: str = Depends(get_authorization_header)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def create_jwt_token(user_id: int):
    payload = {
        "sub": str(user_id),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token
