from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to avoid command injection
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}
    sanitized_host = subprocess.quote(host)
    subprocess.run(['ping', sanitized_host], check=True)
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)