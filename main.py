import models
from fastapi import FastAPI,Depends
from schema import Blog
from database import Engine,SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(Engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/blog")
def create(request:Blog,db:Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title,content=request.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

