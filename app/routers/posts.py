from fastapi import Response,status,HTTPException,Depends,APIRouter
from .. import models,schemas,oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from sqlalchemy import func

router=APIRouter(
     prefix= "/posts",
     tags=['Posts']
)

# @router.get("/")
@router.get("/",response_model=list[schemas.PostOut])
def posts(db: Session = Depends(get_db)):
    

    results=db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(models.Votes,models.Votes.post_id==models.Post.id, isouter=True).group_by(models.Post.id).all()

    return [
    {
        "title": post.title,
        "content": post.content,
        "published": post.published,
        "created_at": post.created_at,
        "user_id": post.user_id,
        "user": post.user,
        "votes": votes
    }
    for post, votes in results
]

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create(post:schemas.createPost,db: Session = Depends(get_db),current_user:int =Depends(oauth2.get_current_user)):
         
    newpost=models.Post(user_id=current_user.id,**post.model_dump())
    db.add(newpost)
    db.commit()
    db.refresh(newpost)
    return newpost

@router.get("/{id}",response_model=schemas.PostOut)
def read(id:int,db: Session = Depends(get_db),):
    # post=db.query(models.Post).filter(models.Post.id==id).first()
    result=db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(models.Votes,models.Votes.post_id==models.Post.id, isouter=True).filter(models.Post.id==id).group_by(models.Post.id).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" post with id {id} does not exist!")

    post,votes= result
    return {
            "title": post.title,
            "content": post.content,
            "published": post.published,
            "created_at": post.created_at,
            "user_id": post.user_id,
            "user": post.user,
            "votes": votes
        }
        


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deletepost(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post=db.query(models.Post).filter(models.Post.id==id)
    if post.first()==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" post with id {id} does not exist!")
    if post.first().user_id != current_user.id:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
         
    post.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Post)
def update(id:int, post: schemas.createPost,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    query=db.query(models.Post).filter(models.Post.id==id)
    update=query.first()
    if update==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" post with id {id} does not exist!")
    query.update(post.model_dump(),synchronize_session=False)

    if update.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    query.update(post.model_dump(),synchronize_session=False)
    db.commit()
    return query.first()