from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run
    if not is_valid_host(host):
        return {"status": "error", "output": "Invalid host"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

def is_valid_host(host: str) -> bool:
    # Add validation logic for the host input
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts