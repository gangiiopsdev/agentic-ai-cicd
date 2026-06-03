from fastapi import FastAPI
import subprocess
g-import os
g-import shlex
g
app = FastAPI()

g@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):
    # Safer implementation
    command = ["ping", *shlex.split(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}