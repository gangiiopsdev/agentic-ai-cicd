from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input host to prevent injection attacks
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host provided."}
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

def is_valid_host(host: str) -> bool:
    # Simple validation to ensure the host is a valid IP address or hostname
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None