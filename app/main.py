from fastapi import FastAPI
import subprocess
import shlex
global_host = '127.0.0.1' # predefined safe host for demonstration purposes
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host != global_host:
        return {'status': 'failed', 'error': 'Unauthorized access'}
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

    return {'status': 'completed'}