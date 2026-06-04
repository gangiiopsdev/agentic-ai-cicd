from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more validation as needed
    return host in allowed_hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):  # Use the validation function
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}