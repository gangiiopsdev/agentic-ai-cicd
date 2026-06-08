from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'status': 'error', 'message': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}