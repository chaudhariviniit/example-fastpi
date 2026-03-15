from fastapi import HTTPException,status,APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database,models,schemas,oauth2,utils
from ..database import get_db

router = APIRouter(tags=['Authentication'])



@router.post("/login",response_model=schemas.Token)
def login(user_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credential.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credential")

    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credential")
    
    access_token = oauth2.create_access_token(data = {"user_id" : user.id })

    return {"access_token": access_token , "token_type" : "bearer"}


        