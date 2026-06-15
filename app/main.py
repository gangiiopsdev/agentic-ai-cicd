from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host input to avoid command injection
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in '.-')
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}