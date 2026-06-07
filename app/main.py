from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use a whitelist of allowed hosts or IP ranges
    allowed_hosts = ['127.0.0.1', '192.168.1.1']
    if host in allowed_hosts:
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'error': str(e)}