from fastapi import APIRouter, Depends,status, Response, HTTPException
from .. import schemas, models, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repo import blog

router = APIRouter(
    prefix = "/blogs",
    tags=["Blog"]
)


get_db = database.get_db

@router.get("/",response_model = list[schemas.ShowBlog])
def All(db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)    


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session = Depends(get_db),current_user: schemas.User =
                                                                    Depends(oauth2.get_current_user)):
    return blog.create(request, db)
    

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)
    


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db:Session = Depends(get_db),current_user: schemas.User =
                                                                            Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
  


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model = schemas.ShowBlog)
def show(id: int, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
    
