from jose import JWTError,jwt
from datetime import datetime,timedelta
from . import schemas,models,database
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

SECRET_KEY = {settings.secret_key}
ACCESS_TOKEN_EXPIRE_MINUTE  = {settings.access_token_expire_minutes}
ALGORITHM = {settings.algorithm}

def create_access_token(data : dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({"exp" : expire})

    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token : str , credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id : str = payload.get("user_id")

        if id is None :
            raise credentials_exception
        token_data = schemas.Tokendata(id = str(id))
        return token_data
    except JWTError:
                raise credentials_exception
    

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    tooken = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == tooken.id).first()
    return user 