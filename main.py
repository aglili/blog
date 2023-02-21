import models
from fastapi import FastAPI
from schema import Blog
from database import Engine

app = FastAPI()

models.Blog.metadata.create_all(Engine)


@app.post("/blog")
def create(request:Blog):
    return request

