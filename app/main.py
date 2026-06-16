from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Define a whitelist of allowed hosts or perform validation
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Host not allowed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)