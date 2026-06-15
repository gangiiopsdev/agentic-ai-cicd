from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    subprocess.call(['ping', host])
    return {'status': 'completed'}