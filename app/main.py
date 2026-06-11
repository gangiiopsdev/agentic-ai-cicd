from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}