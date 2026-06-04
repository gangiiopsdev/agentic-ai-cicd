from fastapi import FastAPI
import subprocess
import shlex
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with command sanitization
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}