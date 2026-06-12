from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    # Secure implementation
    subprocess.call(['ping', host])

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)