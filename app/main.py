from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping_handler(host: str):
    # Validate host input
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    return ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex pattern matching
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None