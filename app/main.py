from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    # Validate host input to prevent command injection
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', quote(host)], check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed", "output": subprocess.run(['ping', quote(host)], check=True, capture_output=True).stdout.decode()})