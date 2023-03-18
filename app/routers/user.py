
from fastapi import APIRouter, status, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, models, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Has the password rom user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    data = models.User(**user.dict())

    db.add(data)
    db.commit()
    # Retrieve just created data
    db.refresh(data)

    return data


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    data = db.query(models.User).filter(models.User.id == id).first()

    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Record does not exist")

    return data
