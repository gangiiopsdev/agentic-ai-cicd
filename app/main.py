from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input further
    if not host or not host.strip():
        return {'status': 'failed', 'error': 'Invalid input'}

    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}