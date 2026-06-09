from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, shell=False, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, shell=False, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}