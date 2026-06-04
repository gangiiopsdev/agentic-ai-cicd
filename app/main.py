from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize the host input
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host], shell=False)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}

def validate_host(host):
    # Add your validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts