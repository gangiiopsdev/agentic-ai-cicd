from fastapi import FastAPI
import subprocess
import shlex

global ping
ping = None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping
    if ping is None:
        args = shlex.split(f'ping {host}')
        ping = subprocess.Popen(args)
    return {"status": "completed"}