from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}