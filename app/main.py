from fastapi import FastAPI
import subprocess
from shlex import quote
from subprocess import Popen, PIPE, CalledProcessError

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        process = Popen(['ping', quote(host)], stdout=PIPE, stderr=PIPE)
        result, error = process.communicate()
        if process.returncode != 0:
            raise CalledProcessError(process.returncode, 'ping', output=error.decode())
        return {'status': 'completed', 'output': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}