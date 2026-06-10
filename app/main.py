from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize and validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid host'}
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}