from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation example: only allow ping to a specific list of hosts
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

@app.get="/ping"
def ping(host: str):
    validate_host(host)
    # Safe implementation using subprocess.run with input sanitization
    sanitized_host = subprocess.quote(host)
    subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed"}