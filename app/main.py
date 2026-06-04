from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize host input
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}

def is_safe_host(host):
    # Implement your validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts