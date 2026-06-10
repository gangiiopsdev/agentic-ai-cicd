from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}