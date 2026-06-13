from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Safe implementation using subprocess.run with proper validation and sanitization
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Validate and sanitize input
    if not host.strip().isalnum() or len(host) > 255:
        raise ValueError("Invalid hostname")
    execute_ping(host)
    return {"status": "completed"}