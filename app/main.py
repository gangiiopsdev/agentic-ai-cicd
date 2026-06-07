from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    return host.isalnum() and '.' not in host

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'invalid input'}
    command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}