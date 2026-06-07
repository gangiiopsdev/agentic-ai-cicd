from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid host name')
app = FastAPI()
@app.get('/ping')
def ping(host: str):\n    # Validate the input to prevent command injection
    validate_host(host)
    try:\n        result = subprocess.run(shlex.split(f'ping {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)\n        return {'status': 'completed', 'output': result.stdout}\n    except subprocess.CalledProcessError as e:\n        return {'status': 'error', 'error': e.stderr}