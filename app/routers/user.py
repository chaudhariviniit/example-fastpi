from .. import models,database,schemas,oauth2, utils
from fastapi import FastAPI,Body,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session 
from ..database import engine,get_db
from ..schemas import PostResponse,PostCreate,UserResponse


router = APIRouter(
    prefix="/users",
    tags=['User']
)


@router.post("/",response_model=schemas.UserResponse)
def create_user (user : schemas.UserCreate,db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/",response_model=list[UserResponse])
def get_user(db: Session = Depends(get_db)):
    show = db.query(models.User).all()
    return show

@router.get("/{id}",response_model=UserResponse)
def get_user(id : int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user == None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"your requested id = {id} is not found")
    else:
        return user
    
