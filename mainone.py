#import 
from fastapi import FastAPI

#instance
app = FastAPI()

#decorator
@app.get("/")
#function
def index():
    return {'data':{'name':'Sarthak'}}

@app.get("/about")
def about():
    return {'data':{'about page'}}