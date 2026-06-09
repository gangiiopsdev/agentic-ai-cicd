from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with full path and validation
    if host in ['google.com', 'example.com']:
        result = subprocess.run(['/usr/bin/ping', host], check=True, text=True)
        return {'status': 'completed', 'result': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}