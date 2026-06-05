from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not (host.replace('.', '').isdigit() or host.startswith('192.168.') or host.startswith('10.')):  # Example of more specific validation
        return {'status': 'failed', 'error': 'Invalid host format'}
    try:
        output = subprocess.run(['ping', '-c', str(4), host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}