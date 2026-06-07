from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Validate and sanitize host input
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Simple validation, replace with more robust checks as needed
    return all(c.isalnum() or c in ('-', '.') for c in host)