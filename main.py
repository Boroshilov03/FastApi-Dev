from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI() #creating  an instance of the FastAPI class. This is our application object

class Post(BaseModel): #validates if title str and content str, valitades schema that the frontend sends to  the backend
    title: str
    content: str
    published: bool = True #if the user doesnt provide published vlaue it will set to true
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content":"content of post 1", "id": 1},
            {"title": "title of post 2", "content":"content of post 2", "id": 2}]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post
@app.get("/") #decorator
def root(): #function
    return {"message": "Welcome"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts} #autom converts to json
                                                        
@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100000)
    my_posts.append(post_dict)
    return {"data": post_dict}
# Schema: title str, content str

@app.get("/posts/{id}") #id is path parameter, making sure id is int
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": post}
