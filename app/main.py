from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation
    try:
        args = ['ping'] + shlex.split(host)
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/', include_in_schema=False)
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    if not host.isalnum() or host.startswith('-'):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)