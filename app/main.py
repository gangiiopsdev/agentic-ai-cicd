from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's a valid hostname or IP address
    if not validate_host(host):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return safe_ping(host)

# Function to validate host input
import re
def validate_host(hostname: str) -> bool:
    # Regular expression to match a valid hostname or IP address
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, hostname) is not None