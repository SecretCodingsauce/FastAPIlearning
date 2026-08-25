from fastapi import status,HTTPException,Depends,APIRouter
from .. import models,schemas,oauth2
from sqlalchemy.orm import Session
from ..database import get_db

router=APIRouter(
    prefix="/vote",
    tags=['Votes']
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post= db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post does not exist")

    vote_query=db.query(models.Votes).filter(models.Votes.post_id==vote.post_id,models.Votes.user_id==current_user.id)
    found_vote=vote_query.first()

    if vote.direction==1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User has liked this already")
        new_vote=models.Votes(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"vote has been added"}

    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "vote deleted successfully"}