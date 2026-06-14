from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host):
    # Validate host input to prevent command injection
    if not validate_host(host):
        raise ValueError('Invalid host')
    try:
        output = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    # Simple validation logic, adjust based on requirements
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}