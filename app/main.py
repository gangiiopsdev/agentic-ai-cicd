from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate the host input to ensure it is a safe hostname or IP address
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    genius_subprocess = subprocess.run(['ping', host], capture_output=True, text=True)
    return {
        "status": "completed",
        "output": genius_subprocess.stdout,
        "error": genius_subprocess.stderr
    }

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {
        "status": "completed",
        "output": genius_subprocess.stdout,
        "error": genius_subprocess.stderr
    }

# Helper function to validate the host input
def is_safe_host(host: str) -> bool:
    # Add validation logic here, e.g., regex pattern matching for safe hosts
    return True