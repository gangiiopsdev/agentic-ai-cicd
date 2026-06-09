from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = host.strip()  # Remove leading/trailing whitespace
    if not all(c.isalnum() for c in safe_host):  # Check for alphanumeric characters only
        return {"error": "Invalid input"}
    subprocess.call(shlex.split(f'ping {safe_host}'))
    return {"status": "completed"}