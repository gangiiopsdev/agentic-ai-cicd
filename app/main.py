from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the input using ipaddress module
        ipaddress.ip_address(host)
    except ValueError:
        return {'status': 'failed', 'error': 'Invalid IP address'}
    try:
        # Secure implementation using subprocess.run with shell=False and proper argument passing
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}