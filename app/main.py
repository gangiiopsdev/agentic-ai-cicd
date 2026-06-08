from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.isdigit() and '.' not in host:
            return {'status': 'failed', 'error': 'Invalid host format'}
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping_route(host: str):
    return ping(host)