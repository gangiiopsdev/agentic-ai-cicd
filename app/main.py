from fastapi import FastAPI
import shlex
import subprocess

def safe_ping(host):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping'] + [arg.strip() for arg in shlex.split(host) if arg.strip()]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)