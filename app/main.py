from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        result = subprocess.run(['ping', '-c 1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    # Add your validation logic here, e.g., using regex or a list of allowed hosts
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) and host in ['example.com']  # Example list