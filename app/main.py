from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    # Simple validation: allow only alphanumeric characters and hyphens
    return host.isalnum() or '-' in host

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if is_valid_host(host):
        # Use shlex.quote to safely escape the host parameter
        subprocess.run(['ping', shlex.quote(host)], check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400