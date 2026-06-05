from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        if not host.strip() or len(host) > 255:
            raise ValueError('Invalid host input')
        output = subprocess.check_output(shlex.split(f'ping {shlex.quote(host)}'), stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}