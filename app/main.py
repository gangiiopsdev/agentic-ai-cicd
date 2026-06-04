from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Validate and sanitize the host input
    if not host.startswith('localhost') and not host.startswith('127.0.0.1'):
        return {'status': 'invalid', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)