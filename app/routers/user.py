from fastapi import APIRouter, Depends,status, Response, HTTPException
from app import schemas, models, database
from app.repo import user
from sqlalchemy.orm import Session


router = APIRouter(
    prefix = "/users",
    tags=["User"]
)

get_db = database.get_db


@router.post("/", response_model = schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db:Session = Depends(get_db)):
    return user.create(request, db)



@router.get("/", response_model = schemas.ShowUser, status_code=status.HTTP_200_OK)
def get_users(id: int, db:Session = Depends(get_db)):
    return user.get_users(id, db)
