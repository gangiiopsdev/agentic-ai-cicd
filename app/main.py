from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    command = ['ping'] + shlex.split(host)
    subprocess.call(command)
app = FastAPI()
@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}