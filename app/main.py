from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host == 'localhost' or host == '127.0.0.1':
        # Sanitize input by escaping special characters
        host = ''.join(c for c in host if c.isalnum() or c in ['-', '.', ':', '/'])
        return subprocess.run(['ping', '-c', '4', host], check=True, capture_output=True)
    else:
        raise ValueError('Invalid host for ping')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'message': 'Ping successful'}
    except ValueError as e:
        return {'status': 'failed', 'message': str(e)}