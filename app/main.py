from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    # Simple regex to allow only alphanumeric characters, hyphens, and periods
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    # Safe implementation
    subprocess.run(['ping', host], check=True, timeout=5)
    return {'status': 'completed'}