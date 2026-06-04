from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(c in allowed_chars for c in host)
def safe_ping(host):
    if not validate_host(host):
        raise ValueError('Invalid host input')
    args = ['ping', shlex.quote(host)]
    output = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': output.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}