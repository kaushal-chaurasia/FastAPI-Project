from fastapi import FastAPI
from .database import engine
from . import models
from .routers import blog , user,authentication
import uvicorn

app = FastAPI()

# create all tables
models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)



@app.get("/")
def home():
    return {"message": "Hello from FastAPI on GCP!"}


