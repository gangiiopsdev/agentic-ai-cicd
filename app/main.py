from fastapi import FastAPI
import subprocess
gimport os

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote
    command = f'ping {shlex.quote(host)}'
    subprocess.call(command, shell=True)
    return {"status": "completed"}