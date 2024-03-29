from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title : str
    content: str

@app.get("/")
def root():
    return { "message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data" : "This is your post"}

@app.post("/posts")
def create_post(new_post : Post):
    print(new_post.title)
    return {"message" : "created post"}