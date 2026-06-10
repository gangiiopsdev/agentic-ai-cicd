from fastapi import FastAPI
import subprocess
app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400