from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid input'}
    # Use a whitelist of allowed hosts or validate the IP address format more strictly
    allowed_hosts = ['127.0.0.1', '::1']  # Example whitelist
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], shell=False, check=True)
    return {'status': 'completed'}