from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run and shlex.quote to prevent shell injection
    safe_host = ' '.join(shlex.quote(arg) for arg in [host])
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation using subprocess.run and shlex.quote to prevent shell injection
    safe_host = ' '.join(shlex.quote(arg) for arg in [host])
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}