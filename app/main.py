from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(filter(lambda c: c.isalnum() or c in ['.', '-'], host))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not all(c.isalnum() or c in ['.', '-'] for c in sanitized_host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}