from fastapi import FastAPI
import subprocess
globally_configured_hosts = ['127.0.0.1'] # Configure a whitelist of allowed hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in globally_configured_hosts:
        # Sanitize input to avoid command injection
        safe_host = subprocess.quote(host)
        subprocess.run(['ping', safe_host], check=True, shell=False)
    else:
        raise ValueError('Invalid host')
    return {'status': 'completed'}