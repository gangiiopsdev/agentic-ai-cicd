from fastapi import FastAPI
import subprocess
from shlex import quote
global app
app = FastAPI()
def safe_ping(host: str):
    if 'ping' in host or any(char.isdigit() for char in host) or len(host) > 255:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', quote(host)], capture_output=True, text=True)
@app.get("/ping")
def ping(host: str):
    safe_ping(host)