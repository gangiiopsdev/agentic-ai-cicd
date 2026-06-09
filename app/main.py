from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' 
    if not all(c in allowed_chars for c in host):
        return {'status': 'failed', 'error': 'Invalid host name'}

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    else:
        return {'status': 'completed', 'output': output.decode()}