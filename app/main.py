from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False
    if host == 'localhost' or host.startswith('127.0.0.1'):
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Invalid host"}