from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        raise ValueError('Invalid hostname')
    # Validate host to ensure it does not contain malicious content
    allowed_hosts = {'example.com', 'test.example.com'}  # Replace with actual validation logic
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    return subprocess.call(['ping', '-c', '1', host], shell=False)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'error': str(e)}