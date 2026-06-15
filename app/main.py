from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with validation and sanitization
    if not host.isalnum() or '@' in host:
        raise ValueError("Invalid host")
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}