from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout if result.returncode == 0 else result.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout if result.returncode == 0 else result.stderr}