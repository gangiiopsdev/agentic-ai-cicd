from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in [',', '.', '-', '_', ':'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_input(host)
    if len(safe_host) != len(host):
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(f'ping {safe_host}')
    return {'status': 'completed'}