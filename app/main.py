from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping'] + shlex.split(host)
    return subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict):
        return result
    else:
        return {'status': 'completed'}