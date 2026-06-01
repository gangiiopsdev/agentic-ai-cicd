from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.run instead of subprocess.call and avoid shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not validate_host(host):
        raise ValueError("Invalid host")
    response = safe_ping(host)
    return {"status": "completed", "response": response}

def validate_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts