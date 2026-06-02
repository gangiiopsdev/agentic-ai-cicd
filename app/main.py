from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safer implementation using subprocess.run with list arguments and input validation
    allowed_hosts = ['google.com', 'example.com']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        try:
            subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}