from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Unauthorized host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)