from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.replace('.', '').isalnum() or '@' in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)