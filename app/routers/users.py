from fastapi import status,HTTPException,Depends,APIRouter
from .. import models,schemas,security
from sqlalchemy.orm import Session
from ..database import get_db

router=APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/newuser", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def createUser(user: schemas.User,db:Session=Depends(get_db)):
    user_data = user.model_dump()

    user_data["password"] = security.password_hasher.hash(user.password)

    newuser = models.User(**user_data)

    db.add(newuser)
    db.commit()
    db.refresh(newuser)

    return newuser

@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" user with id {id} does not exist!")
    return user