from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with input validation and sanitization
    if host == 'localhost':
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}