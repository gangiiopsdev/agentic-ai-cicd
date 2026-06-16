from fastapi import FastAPI
import subprocess
import re
import shlex

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host name'}, 400
    # Secure implementation using subprocess.run to safely handle arguments
    result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True)
    if result.returncode == 0:
        return {'status': 'completed'}
    else:
        return {'error': 'Ping failed'}, 500