from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host or ' ' in host:
        raise ValueError('Invalid input')
    # Sanitize the host parameter by escaping special characters
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in ('.', ':', '-', '_'))
    subprocess.call(['ping', sanitized_host])
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}