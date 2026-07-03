from fastapi import FastAPI, Request, Form
from database import engine, Base, SessionLocal
from models import Task
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


# open application
app = FastAPI()


# 
Base.metadata.create_all(bind=engine)


app.mount("/static", StaticFiles(directory="static"), name="static")


# Import any file into templates
templates = Jinja2Templates(directory="templates")





# Bring the homepage
@app.get("/", response_class = HTMLResponse)

def home(request:Request): # function
    db = SessionLocal() # Open a connection to the database

    tasks = db.query(Task).all() # Bring all the tasks

    db.close() # close database

    return templates.TemplateResponse(
        request=request,
        name = "index.html",
        context={"tasks":tasks}
    )




# Add tasks
@app.post("/tasks")

def create_tasks(title:str = Form(...)):

    db = SessionLocal()


    task = Task(
    
        title=title,
        
    )

    db.add(task)
    db.commit()
    db.close()

    return RedirectResponse("/tasks", status_code=303)




# Bring all the tasks
@app.get("/tasks", response_class=HTMLResponse)

def tasks_page(request:Request):

    db = SessionLocal()

    tasks = db.query(Task).all()

    db.close()

    return templates.TemplateResponse(
        request=request,
        name="tasks.html",
        context={"tasks":tasks}
    )

# method GET / delete
@app.get("/delete/{id}")


def delete_task(id:int):

    db = SessionLocal()

    task = db.query(Task).filter(Task.id == id).first()

    if task:
     db.delete(task)
     db.commit()
    
    db.close()

    return RedirectResponse("/tasks", status_code=303)




# method GET / complete
@app.get("/complete/{id}")
def complate_task(id:int):
   db = SessionLocal()

   task = db.query(Task).filter(Task.id == id).first()

   if task:
      task.done= True
      db.commit()
    
   db.close()

   return RedirectResponse("/tasks", status_code=303)




#  method GET / Edit
@app.get("/edit/{id}", response_class=HTMLResponse)
def Edit_task(id:int, request:Request):
   
   db = SessionLocal()

   task = db.query(Task).filter(Task.id == id).first()
   db.close()

   return templates.TemplateResponse(
      request=request,
      name="edit.html",
      context={"task":task}
   )




@app.post("/update/{id}")
def update_task(id:int,
                title:str = Form(...)
                
):
   db = SessionLocal()

   task = db.query(Task).filter(Task.id == id).first()

   if task:
      task.title = title
      db.commit()

   db.close()

   return RedirectResponse("/tasks", status_code=303)