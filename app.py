from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import time


#define base model
class BaseTodo(BaseModel):
    task: str


#define model:
class TodoModel(BaseTodo):
    id: Optional[int] = None
    is_complete: bool = False


class ReturnModel(BaseModel):
    task: str




app = FastAPI()

to_do = []

# write a first middleware

@app.middleware("http")
async def log_middleware(request, call_next):
    start_time =  time.time()
    response  = await call_next(request)
    end_time = time.time()
    processed_time =  end_time - start_time
    print(f"Total time required for Request {request.url} is {processed_time} seconds")
    return response




#create a todo
@app.post("/todos", response_model=ReturnModel)
async def add_todo(todo: TodoModel):
    todo.id = len(to_do)+1
    to_do.append(todo)
    return todo

#query parameters

#read all todos
@app.get("/todos")
async def read_todos(completed: Optional[bool]=None):
    if completed is None:
        return to_do
    else:
        return [todo_task  for todo_task in to_do if todo_task.is_complete == completed]
    # return to_do


#Get a todo
@app.get("/todos/{id}")
async def read_todo(id: int):
    for todo in to_do:
        if todo.id ==  id:
            return todo
        
    raise HTTPException(status_code=404, detail="Does not Exist")


# for update a record
@app.put("/todos/{id}")
async def update_todo(id: int, new_todo: TodoModel):
    for index, todo in enumerate(to_do):
        if todo.id == id:
            to_do[index] = new_todo
            to_do[index].id = id
            return "Item updated successfully"
    raise HTTPException(status_code=404, detail="Does not Exist")

#for deleting a record
@app.delete("/todos/{id}")
async def delete_todo(id: int):
    for index, todo in enumerate(to_do):
        if todo.id ==  id:
            del to_do[index]
            return "Item deleted successfully"
    raise HTTPException(status_code=404, detail="Does not Exist")
        

        
    