from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> bool:
    return host.isalnum() and '.' not in host

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not sanitize_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}