from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(["ping", host])
    return {"status": "completed"}

def is_valid_host(hostname: str) -> bool:
    # Basic validation of hostname (example)
    return all(c.isalnum() or c in ".-_" for c in hostname)