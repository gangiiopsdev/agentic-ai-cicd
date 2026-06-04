from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Define a list of allowed hosts or use regex to validate host input
def is_valid_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

def execute_ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host format')
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    return result