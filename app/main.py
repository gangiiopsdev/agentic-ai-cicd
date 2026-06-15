from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize host input
    if not isinstance(host, str) or not re.match(r'^[a-zA-Z0-9.-_]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping', subprocess.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}