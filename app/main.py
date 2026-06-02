from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add your validation logic here (e.g., allowed IP ranges)
    if not host.isdigit():
        raise ValueError('Invalid host input')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': result.stdout}