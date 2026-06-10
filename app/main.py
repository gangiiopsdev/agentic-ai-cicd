from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)