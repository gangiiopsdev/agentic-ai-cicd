from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host):
    if host.isnumeric() and len(host) <= 3:
        # Safe ping implementation using list arguments with shell=False
        args = ['ping', '-c', '1'] + shlex.split(host)
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric() or len(host) > 3:
        return {"error": "Invalid input"}, 400
    safe_ping(host)
    return {"status": "completed"}