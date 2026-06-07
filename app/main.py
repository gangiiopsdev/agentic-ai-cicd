from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        subprocess.run(['ping', host], check=True)
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'error': f'Ping failed: {e}'}

    return {'status': 'completed'}