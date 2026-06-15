from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host name')
    safe_ping(host)
    return {'status': 'completed'}