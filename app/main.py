from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        args = ['ping'] + shlex.split(host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode('utf-8')}
    return {'status': 'completed', 'output': output.decode('utf-8')}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    if not host.isalnum() or '.' not in host:
        return {'error': 'Invalid host'}
    return ping(host)