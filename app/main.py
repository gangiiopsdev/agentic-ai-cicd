from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)