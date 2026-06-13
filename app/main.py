from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

allowed_hosts = {'example.com', 'localhost'}

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)