from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    parts = host.split('.').copy()
    return len(parts) == 2 and all(part.isalnum() for part in parts)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if is_valid_host(host):
        try:
            subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}
    else:
        return {'status': 'invalid input'}
    return {'status': 'completed'}