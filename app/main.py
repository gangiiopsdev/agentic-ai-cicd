from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host or len(host.split('.')) != 4:
        return {'error': 'Invalid host'}, 400
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}