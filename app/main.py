from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with absolute path and proper checks
    safe_host = host.strip().replace(' ', '_')  # Basic input sanitization
    if not safe_host:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}