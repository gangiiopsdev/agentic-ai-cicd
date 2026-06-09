from fastapi import FastAPI
import subprocess
import shlex

global host
host = '127.0.0.1'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping():
    command = ['ping', host]
    subprocess.call(command)
    return {"status": "completed"}