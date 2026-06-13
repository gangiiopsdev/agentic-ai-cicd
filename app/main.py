from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not validate_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    return ping(host)

def validate_host(host: str) -> bool:
    # Implement validation logic, e.g., check for allowed domain names or IP addresses
    return True