from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to avoid command injection
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}
    try:
        sanitized_host = subprocess.run(['ping', '--', host], capture_output=True, text=True, check=True)
        return sanitized_host.stdout
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)