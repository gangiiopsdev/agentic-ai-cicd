from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize host to prevent command injection
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True, capture_output=True)
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}