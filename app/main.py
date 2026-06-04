from fastapi import FastAPI
import subprocess
import shlex
g-import os
app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):
    # Safer implementation
    if not host.strip().startswith('-'):
        command = ["ping", *shlex.split(host)]
        subprocess.run(command, check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid input detected"}