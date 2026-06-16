from fastapi import FastAPI
import subprocess
import shlex
global args
args = []

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global args
    safe_host = shlex.quote(host)
    args.append(f'ping {safe_host}')
    return {"status": "completed"}