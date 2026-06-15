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
    # Secure implementation using shlex.quote to avoid command injection
    subprocess.call(shlex.split(f'ping {shlex.quote(host)}')))
    return {"status": "completed"}