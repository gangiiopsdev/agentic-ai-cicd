from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host name")
    sanitized_host = subprocess.list2cmdline([host])
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}