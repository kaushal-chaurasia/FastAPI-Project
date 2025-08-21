from fastapi import FastAPI

import uvicorn
from blog import models, database
from blog.database import engine
from blog.routers import blog_routes, user, authentication



app = FastAPI()

# create all tables
models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog_routes.router)
app.include_router(user.router)



@app.get("/")
def home():
    return {"message": "Hello from FastAPI on GCP!"}


