from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid hostname"}
    command = shlex.split(f"ping {host}")
    try:
        subprocess.run(command, check=True)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}