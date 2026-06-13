from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.split to safely split the command
    subprocess.call(shlex.split(f'ping {shlex.quote(host)}')))
    return {"status": "completed"}