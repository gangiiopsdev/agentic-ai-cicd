from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run with shell=False and validation
    args = ['ping', host]
    if not all(c.isalnum() or c in '-.' for c in host):  # Basic validation of the hostname
        raise ValueError('Invalid host name')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'stdout': result.stdout, 'stderr': result.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)