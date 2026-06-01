from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add your validation logic here
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed'}