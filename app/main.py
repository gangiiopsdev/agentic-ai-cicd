from fastapi import FastAPI
import subprocess
def safe_ping(host):
    return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid input')
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}