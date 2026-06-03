from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    if not all(c.isalnum() or c in ['.'] for c in host):
        raise ValueError('Invalid hostname')
    return subprocess.run(args, capture_output=True, shell=False)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in ['.'] for c in host):
        raise ValueError('Invalid hostname')
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}