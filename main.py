from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel,EmailStr,Field
from typing import Annotated
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")
class User(BaseModel):
    name:Annotated[str,Field(...,description="enter the name",example="aahan")]
    email:Annotated[EmailStr,Field(...,description="enter the email",example="abc@gmail.com")]
    
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
@app.get("/search")
def search_users(name:str,request:Request):
    with open("users.json", "r") as f:
        data = json.load(f)
        results = []
        for dat in data:
            if name==dat["name"]:
                results.append(dat)
        return templates.TemplateResponse(
            "users.html",
            {
            "request": request,
            "users": results
        }
    )
@app.get("/search_page")
def search_page(request: Request):
    return templates.TemplateResponse(
        "search.html",
        {"request": request}
    )
        
@app.get("/users")
def show_users(request: Request):

    with open("users.json", "r") as f:
        data = json.load(f)

    return templates.TemplateResponse(
        "users.html",
        {
            "request": request,
            "users": data
        }
    )
@app.post("/submit")
def submit(
    name: str = Form(...),
    email: str = Form(...)
):
    with open("users.json","r") as f:
        data =json.load(f)
    data.append( {
        "name": name,
        "email": email
    }
    )
    with open("users.json","w") as f:
        json.dump(data, f, indent=4)
    return{
        "message":"user added successfully",
        "name":name,
        "email":email
    }

@app.post("/user_info")
def get_input(user:User):
    with open("users.json","r") as f:
        data = json.load(f)
    data.append({"name":user.name,
           "email":user.email})
    with open("users.json", "w") as f:
                json.dump(data, f, indent=4)
    return{
          "name":user.name,
          "email":user.email
    }
@app.get("/user_data")
def get_data():
    with open("users.json","r") as f:
        data = json.load(f)
    return data
@app.put("/user_update")
def get_update(email:EmailStr,user:User):
    with open("users.json","r") as f:
        data = json.load(f)
    for index,dat in enumerate(data):
        if email==dat["email"]:
            data[index] = user.model_dump()
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)
    return{"message":"user updated"}
@app.get("/user_delete")
def get_delete(email:EmailStr):
    with open("users.json","r") as f:
        data = json.load(f)
    for index,d in enumerate(data):
         if email==d["email"]:
              data.pop(index)
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)
    return{"message":"successfully done"}


              

         