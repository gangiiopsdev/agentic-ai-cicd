from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in '.-' for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}