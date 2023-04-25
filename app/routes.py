from flask import Flask, request
from datetime import datetime 
from app.database import task

app = Flask(__name__)

@app.get("/")
def ping():
    return{
        "status": "ok",
        "message": "pong",
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }

@app.get("/tasks")
def get_all_tasks():
    tasks = task.scan()
    out = {
        "status": "ok",
        "tasks": tasks
    }
    return out

@app.get("/tasks/<int:pk>")
def get_task_by_id(pk):
    single_task= task.select_by_id(pk)
    out = {
        "status": "ok",
        "task": single_task
    }
    return out

@app.put("/tasks/<int:pk>")
def update_task_by_id(pk):
    raw_data = request.json
    task.update_by_id(pk, raw_data)
    return "", 204

@app.delete("/task/<int:pk>")
def delete_by_id(pk):
    task.delete_by_id(pk)
    return "", 204

@app.post("/tasks")
def create_task():
    raw_data = request.json
    task.create(raw_data)
    out = {
        "status": "ok",
        "message": "created"
    }   
    return out, 201