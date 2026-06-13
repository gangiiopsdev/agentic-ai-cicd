from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not all(c.isalnum() or c in '.-' for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        # Safer implementation using subprocess.run
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}