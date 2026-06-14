from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.isalnum() and not host.startswith('192.168') and not host.startswith('172.16') and not host.startswith('10.'):  # Example validation rules
        raise ValueError("Invalid hostname")
    return True

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'error': 'Invalid hostname'}