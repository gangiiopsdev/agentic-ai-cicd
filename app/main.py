from fastapi import FastAPI
import subprocess
import shlex

global args
args = shlex.split('ping 127.0.0.1')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(args)
    return {"status": "completed"}