from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host or not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}