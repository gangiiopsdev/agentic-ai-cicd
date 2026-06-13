from fastapi import FastAPI
import subprocess
import shlex
cmd = ['ping', host]
args = shlex.split(' '.join(cmd))
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not host.isalnum() and not all(c in '-.' for c in host):
            return {'status': 'failed', 'error': 'Invalid host name'}
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}