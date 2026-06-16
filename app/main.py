from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', '127.0.0.1']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)