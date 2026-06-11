from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host provided"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., check if the host is in a whitelist
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return pattern.match(host) is not None