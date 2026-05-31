from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(c for c in host if c.isalnum() or c in [',', '.', ' ', '-', '_'])

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in [',', '.', ' ', '-', '_'] for c in sanitized_host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}