from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host == 'localhost' or host == '127.0.0.1':
        return subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid host for ping')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        if '100% packet loss' in result.stdout:
            return {'status': 'failed', 'message': 'Ping failed'}
        else:
            return {'status': 'completed', 'message': 'Ping successful'}
    except ValueError as e:
        return {'status': 'failed', 'message': str(e)}