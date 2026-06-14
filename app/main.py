from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Change method name to avoid conflict with built-in 'ping'
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}