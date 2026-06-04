from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isdigit():
        return "Invalid host"
    return subprocess.call(['ping', host])
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if result == 0:
        return {'status': 'completed', 'result': 'success'}
    else:
        return {'status': 'failed', 'result': 'error'}