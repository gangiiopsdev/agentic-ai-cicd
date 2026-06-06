from fastapi import FastAPI
import subprocess
import re
def sanitize_host(host: str):
    return ''.join(e for e in host if e.isalnum() or e in '.-')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        command = ['ping', '--', sanitized_host]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Ping failed: {e.stderr}'}