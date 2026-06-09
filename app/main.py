from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        args = ['ping', *shlex.split(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return {'status': 'completed' if result.returncode == 0 else 'failed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

# Preventive controls: Validate or sanitize the input to ensure it does not contain malicious content.
def validate_host(host):
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping_validated(host: str):
    try:
        validate_host(host)
        args = ['ping', *shlex.split(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return {'status': 'completed' if result.returncode == 0 else 'failed', 'output': result.stdout}
    except ValueError as e:
        return {'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}