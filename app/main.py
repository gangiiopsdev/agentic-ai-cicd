from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    # Implement logic to validate the host
    return host in ['allowed.host1', 'allowed.host2']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', host], timeout=10, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.output.decode()}