from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(host):
    return host.isalnum()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}