from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = sanitize_host(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {"error": "Invalid hostname"}
    subprocess.run(["ping", sanitized_host], check=True, shell=False)
    return {"status": "completed"}