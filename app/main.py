from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate host input to prevent command injection
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

# Define a function to validate the host input
import re

def is_valid_host(host: str) -> bool:
    # Simple regex to allow alphanumeric characters and hyphens, and limit length
    pattern = r'^[a-zA-Z0-9-]{1,255}$'
    return re.match(pattern, host) is not None