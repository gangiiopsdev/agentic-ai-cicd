from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}