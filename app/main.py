from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host or '&&' in host or ';' in host:
        raise ValueError('Invalid host name')
    return host

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and safe arguments
    sanitized_host = safe_ping(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}