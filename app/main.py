from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host: str):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

def sanitize_input(input_str: str):
    return input_str.strip().replace(';', '').replace('&', '')

@app.get('/ping')
def ping_endpoint(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', '-c 1', f'"{sanitized_host}"'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}