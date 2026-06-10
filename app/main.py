from fastapi import FastAPI
import subprocess
import os
g import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with proper argument handling and input validation
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host parameter")
    result = subprocess.run(['ping', '-c', '1', f'"{host}"'], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}