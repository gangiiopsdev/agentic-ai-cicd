from fastapi import FastAPI
import subprocess
def sanitize_host(host: str):
    if not host.isalnum():
        return False
    return True

app = FastAPI()

def ping(host: str):
    if not sanitize_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    if not sanitize_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    return ping(host)