from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    sanitized_host = host.strip()
    if not all(c.isalnum() or c in ['.', '-'] for c in sanitized_host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}