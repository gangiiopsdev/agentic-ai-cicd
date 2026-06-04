from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize the host input
    if 'ping' in host or '|' in host:
        raise ValueError('Invalid input')
    return subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}