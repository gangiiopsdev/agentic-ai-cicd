from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

def is_valid_host(host: str):
    # Add your validation logic here
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)