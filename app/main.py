from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Regex to validate host input
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def is_valid_host(host: str) -> bool:
    # Placeholder for actual validation logic
    return True