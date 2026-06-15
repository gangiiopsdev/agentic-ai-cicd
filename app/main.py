from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host or len(host) > 255:
        return {'status': 'error', 'error': 'Invalid host name'}
    try:
        command = ['ping'] + shlex.split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode()}