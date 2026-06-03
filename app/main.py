from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input to prevent command injection
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    result = subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}

def is_valid_host(host: str) -> bool:
    # Simple validation example: only allow alphanumeric characters and periods
    return all(c.isalnum() or c == '.' for c in host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    result = subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}