from fastapi import FastAPI
import subprocess
from shlex import quote
from subprocess import Popen, PIPE

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize user input
    if not host.isalnum() or len(host) > 64:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        process = Popen(['ping', '-c', '1', '--', quote(host)], stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if process.returncode != 0:
            return {'status': 'failed', 'error': str(error.decode('utf-8'))}
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}