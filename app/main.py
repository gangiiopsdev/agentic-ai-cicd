from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation with validation
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Unauthorized host'}, 403

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return ping(host)