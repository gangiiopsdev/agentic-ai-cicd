from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Safe implementation using subprocess.run with a sanitized host
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Call the safe function to avoid shell=True
    if validate_host(host):
        safe_ping(host)
        return {"status": "completed"}
    else:
        return {"status": "Invalid host"}, 400

def validate_host(host: str) -> bool:
    # Add validation logic here to ensure the host is safe
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None