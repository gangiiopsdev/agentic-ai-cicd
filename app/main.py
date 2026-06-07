from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    if host.strip() and all(c.isalnum() or c in '-.' for c in host):
        return True
    return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        raise ValueError('Invalid host name')
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}