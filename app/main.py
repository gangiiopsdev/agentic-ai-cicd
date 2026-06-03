from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    if '/' in host or ';' in host:
        raise ValueError('Invalid input')
    subprocess.call(['ping', host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}