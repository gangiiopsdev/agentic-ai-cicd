from fastapi import FastAPI
import subprocess
from ipaddress import ip_address

def gethostbyname(host):
    try:
        return str(ip_address(host))
    except ValueError:
        raise ValueError('Invalid IP address')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(['ping', gethostbyname(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}