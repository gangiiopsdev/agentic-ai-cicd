from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    cimport = ('ping', host)
    result = subprocess.run(cimport, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host to prevent OS command injection
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    return ping(host)