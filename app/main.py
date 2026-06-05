from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input
    allowed_hosts = ['google.com', 'facebook.com']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)