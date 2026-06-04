from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Regex to allow only alphanumeric characters and periods/hyphens
        raise ValueError('Invalid host value')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)