from fastapi import FastAPI,Body,Response,status,HTTPException,Depends,APIRouter
from .. import models,database,schemas,oauth2, utils
from sqlalchemy.orm import Session
from ..database import engine,get_db


router = APIRouter(
    prefix="/votes",
    tags=["Vote"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote,
         db: Session = Depends(database.get_db),
         current_user : models.User = Depends(oauth2.get_current_user)):
    
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()

    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=(f"{current_user.email} is already liked post of {vote.post_id}"))
        added_vote=models.Vote(post_id = vote.post_id , user_id = current_user.id)
        db.add(added_vote)
        db.commit()
        return {"Message" : "vote is sucessfully added"}
    else :
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"your requested {vote.post_id} is not found")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"Message" : "Successfully removed vote"}