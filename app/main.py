from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> bool:
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not sanitize_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        command = shlex.split(f'ping {host}')
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}