from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host is a valid IP address or domain name
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "invalid_host"}
    subprocess.run(["ping", host], check=True, capture_output=True)
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)