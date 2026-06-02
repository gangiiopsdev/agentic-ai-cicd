from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], shell=False, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

def validate_host(host: str) -> bool:
    # Add logic to validate the host input
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts