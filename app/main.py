from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation
    command = ['ping'] + shlex.split(host)
    subprocess.call(command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ['ping'] + shlex.split(host)
    subprocess.call(command)
    return {"status": "completed"}