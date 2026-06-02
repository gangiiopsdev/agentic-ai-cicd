from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    valid_hosts = ['google.com', 'example.com']  # Define a list of allowed hosts
    if host in valid_hosts:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}