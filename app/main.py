from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's a safe hostname or IP address
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    subprocess.call(["ping", host])
    return {"status": "completed"}

def is_safe_host(host: str) -> bool:
    # Implement your validation logic here (e.g., regex, allowed hosts list)
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None