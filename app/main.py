from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent shell injection
    if not all(c.isalnum() or c in '.:-' for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}
    return {'status': 'completed', 'output': output.decode('utf-8')}