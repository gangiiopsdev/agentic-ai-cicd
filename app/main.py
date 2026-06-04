from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host input
    if not host.strip() or len(host) > 256:
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/"")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get="/ping")
def ping(host: str):
    # Validate the host input
    if not host.strip() or len(host) > 256:
        raise ValueError("Invalid host")
    safe_ping(host)
    return {"status": "completed"}