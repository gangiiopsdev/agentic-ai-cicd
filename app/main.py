from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/ping')
def ping(host: str):
    if not host.startswith('localhost') and not host.startswith('127.0.0.1'):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return secure_ping(host)