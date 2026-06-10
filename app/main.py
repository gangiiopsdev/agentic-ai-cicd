from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']  # List of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}