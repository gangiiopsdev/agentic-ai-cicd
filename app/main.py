from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {"status": "failed", "error": "Invalid host name"}
    command = ['ping', shlex.quote(host)]
    subprocess.call(command, shell=False)
    return {"status": "completed"}