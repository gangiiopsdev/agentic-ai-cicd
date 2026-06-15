from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote
    command = f'ping {shlex.quote(host)}'
    subprocess.run(command, shell=False)
    return {"status": "completed"}