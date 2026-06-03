from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate input to prevent injection attacks
        if not host.isalnum():
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}