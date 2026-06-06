from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Validate and sanitize host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}