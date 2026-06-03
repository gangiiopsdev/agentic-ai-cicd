from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if 'ping' in host or '--help' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.run(['ping', '-c', 1, host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)