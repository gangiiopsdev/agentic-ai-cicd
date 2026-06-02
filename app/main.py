from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's safe to ping
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed domain names or IP addresses
    pattern = r'^([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.)+[a-zA-Z]{2,}$'
    return re.match(pattern, host) is not None