from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Regular expression to validate host input
def is_valid_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host input')
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)