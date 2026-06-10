from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    # Sanitize host input to avoid command injection
    if '/' in host or '\' in host:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', quote(host)], check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}