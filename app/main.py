from fastapi import FastAPI
import subprocess

app = FastAPI()

ALLOWED_HOSTS = ['example.com', 'test.com']

def safe_ping(host: str):
    if host not in ALLOWED_HOSTS:
        return "Invalid host"
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'error', 'output': 'Invalid host'}
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}