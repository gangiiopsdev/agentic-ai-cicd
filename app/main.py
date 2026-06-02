from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str):
    if not host.isalnum() or len(host) > 255:
        return False
    return True

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid input'}
    host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}