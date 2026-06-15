from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host name'}, 400
    # Secure implementation using shlex to safely handle arguments
    subprocess.call(['ping', *shlex.split(host)], shell=False)
    return {'status': 'completed'}