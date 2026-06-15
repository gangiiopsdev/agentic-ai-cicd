from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        return host
    raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_host(host))
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}