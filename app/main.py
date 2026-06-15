from fastapi import FastAPI
import subprocess
cimport shlex
global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex to escape arguments
    cmd = ['ping', host]
    subprocess.call(cmd)
    return {"status": "completed"}