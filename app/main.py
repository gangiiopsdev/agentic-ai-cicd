from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Sanitize input to prevent command injection
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    return subprocess.run(['ping', host], capture_output=True, text=True, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = secure_ping(host)
    if 'status' in result and result['status'] == 'failed':
        return result
    try:
        output = result.stdout
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}