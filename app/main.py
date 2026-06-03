from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}