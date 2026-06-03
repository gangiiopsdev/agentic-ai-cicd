from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate input to ensure it does not contain malicious commands
        allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
        if any(char not in allowed_chars for char in host):
            raise ValueError('Invalid input')
        result = subprocess.run(['ping'] + shlex.split(shlex.quote(host)), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():  # Simplified validation
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)