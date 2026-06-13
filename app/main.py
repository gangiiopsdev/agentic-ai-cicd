from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    return host in allowed_hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        try:
            subprocess.run(['ping', host], check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Invalid host'}