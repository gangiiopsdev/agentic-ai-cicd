from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ['localhost', '127.0.0.1']:
        return subprocess.call(['ping', '--', host])
    else:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'error': str(e)}