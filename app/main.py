from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isalnum():
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host name')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)