from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}