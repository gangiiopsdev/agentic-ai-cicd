from fastapi import FastAPI
import subprocess
from shlex import quote
global ALLOWED_HOSTS
ALLOWED_HOSTS = ['example.com', 'localhost']
app = FastAPI()
def sanitize_host(host):
    if host not in ALLOWED_HOSTS:
        raise ValueError('Invalid host')
@app.get("/ping")
def ping(host: str):
    sanitize_host(host)
    result = subprocess.run(['ping', quote(host)], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}