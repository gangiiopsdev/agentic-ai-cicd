from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    if not host or len(host) > 255:
        raise ValueError('Invalid host parameter')
    return ''.join(c for c in host if c.isalnum() or c in '.-:/')

@app.get('/ping')
def ping(host: str):
    sanitized_host = validate_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}