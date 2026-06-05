from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        return {"status": "error", "output": "Invalid host"}
    command = ["ping", *shlex.split(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

# Example validation function (replace with actual validation logic)
def validate_host(host: str) -> bool:
    return host.strip().isalnum() and len(host.split('.')) == 4}