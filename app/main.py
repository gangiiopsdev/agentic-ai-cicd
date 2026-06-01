from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using shlex.quote to sanitize input
    subprocess.call(f'ping {quote(host)}')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}