from fastapi import FastAPI
import subprocess
from ipaddress import ip_address

def gethostbyname(host):
    try:
        return str(ip_address(host))
    except ValueError:
        raise ValueError('Invalid IP address')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not ip_address(host).is_private:
        raise ValueError('Invalid IP address')
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}