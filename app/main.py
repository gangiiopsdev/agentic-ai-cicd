from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is a valid hostname or IP address
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}, 400
    subprocess.call(["ping", host])
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Implement a function to validate the host input
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None