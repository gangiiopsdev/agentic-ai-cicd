from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        response = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return {'status': 'completed', 'output': response.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/ping')
def ping_wrapper(host: str):
    # Validate input to ensure it does not contain malicious content
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host name'}
    return ping(host)