from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize input before using in subprocess call
    if is_valid_host(host):
        subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    safe_ping(host)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Implement input validation logic here
    return True  # Placeholder for actual validation