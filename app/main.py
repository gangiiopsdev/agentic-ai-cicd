from fastapi import FastAPI
import subprocess
from typing import Dict

def sanitize_input(user_input: str) -> str:
    # Implement proper sanitization logic here
    return ''.join(char for char in user_input if char.isalnum() or char in ['-', '.', '_', '/'])

app = FastAPI()

@app.get('/ping', response_model=Dict)
def ping(host: str) -> Dict:
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run with shell=False and check=True
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}