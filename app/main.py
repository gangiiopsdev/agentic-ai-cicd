from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using shlex.quote to sanitize input
    quoted_host = quote(host)
    if 'ping' not in quoted_host:
        raise ValueError('Invalid command detected')
    subprocess.call(['ping', quoted_host])

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}