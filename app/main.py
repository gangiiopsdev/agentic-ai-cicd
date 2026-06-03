from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ['ping', shlex.quote(host)]  # Sanitize input using shlex.quote
    subprocess.run(command, check=True)
    return {"status": "completed"}