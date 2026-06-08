from fastapi import FastAPI
import subprocess
def safe_execute_command(host):
    command = ['ping', host.strip()]
    return subprocess.run(command, capture_output=True, text=True)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Validate input to ensure it's a safe hostname
    if not host.strip().isalnum() or '.' in host:
        raise ValueError('Invalid hostname')
    result = safe_execute_command(host)
    return {'status': 'completed', 'output': result.stdout}