from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input by checking if the host is a valid IP address or hostname
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Simplified regex for demonstration purposes
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}