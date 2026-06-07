from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and input validation
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}