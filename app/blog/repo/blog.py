from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, status
from starlette.responses import Response

from .. import models, schemas, hashing


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id= 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def update(id: int, request: schemas.Blog, db:Session):
    blog =  db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")

    update_data = request.dict()
    update_data.pop("published", None)
    blog.update(update_data, synchronize_session=False)
    db.commit()
    return {"message": "Blog updated successfully"}


def show(id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog