from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using shlex.split to safely construct the command
    command = ['ping', host]
    subprocess.call(command)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}