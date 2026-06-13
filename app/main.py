from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and explicit arguments
    if host.strip() != host or not all(c in string.ascii_letters + string.digits for c in host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}