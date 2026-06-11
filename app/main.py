from fastapi import FastAPI
import subprocess
import re

def is_valid_host(host: str) -> bool:
    valid_hosts = ['example.com', 'test.com']
    return host in valid_hosts and re.match(r'^[a-zA-Z0-9.-]+$', host)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '-c 4', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

# Secure Fix: Avoid using shell=True and use a safe method to validate input