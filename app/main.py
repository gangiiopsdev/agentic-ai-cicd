from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError("Invalid input")

    command = ["ping", *shlex.split(shlex.quote(host))]
    subprocess.run(command, check=True)

    return {"status": "completed"}