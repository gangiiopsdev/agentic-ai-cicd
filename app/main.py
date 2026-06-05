from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation: allow only alphanumeric characters and some special characters
    return all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        try:
            subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}