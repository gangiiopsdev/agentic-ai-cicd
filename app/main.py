from fastapi import FastAPI
import subprocess
import re

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in '.-')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host parameter to ensure it only contains allowed characters and format
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    sanitized_host = sanitize_input(host)
    try:
        # Use a safe command with parameters to avoid shell=True and potential injection
        result = subprocess.run(['ping', '-c', 4, sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}