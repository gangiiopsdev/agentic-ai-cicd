from fastapi import FastAPI
import subprocess
import shlex
import os

current_user = os.getenv('USER')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with user input sanitization
    args = shlex.split(f'ping -c 1 {shlex.quote(host)}')
    subprocess.run(args, check=True)
    return {"status": "completed"}