from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        # Validate input to prevent command injection
        if not host.isalnum():
            return {'status': 'failed', 'error': 'Invalid host name'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}