from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid characters in host name')
global_args = ['ping', shlex.quote(host)]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(global_args, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}