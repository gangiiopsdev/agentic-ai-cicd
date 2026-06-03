from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "invalid input"}, 400
    args = ['ping', host]
    subprocess.call(shlex.split(' '.join(args)))
    return {"status": "completed"}