from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate input to avoid injection attacks
        if not host.isalnum() or len(host) > 64:
            raise ValueError('Invalid hostname')
        result = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'result': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}