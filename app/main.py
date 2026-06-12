from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess.run with args to avoid shell injection
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's safe
    if not host.isalnum() or '.' not in host:
        raise ValueError("Invalid host")
    result = safe_ping(host)
    return {"status": "completed", "output": result}