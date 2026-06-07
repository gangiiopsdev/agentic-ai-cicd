from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it is safe to ping
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        args = shlex.split(f'ping -c 1 --nameserver {host}')
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}