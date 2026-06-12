from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Safe implementation
    args = shlex.split('ping ' + host)
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    args = shlex.split('ping ' + host)
    subprocess.call(args)
    return {"status": "completed"}