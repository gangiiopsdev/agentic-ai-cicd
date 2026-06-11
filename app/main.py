from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    subprocess.call(command)
    return {"status": "completed"}