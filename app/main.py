from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    valid_hosts = ['127.0.0.1', '8.8.8.8']
    if host in valid_hosts:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)