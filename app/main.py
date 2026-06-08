from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ['.', '-'])

def validate_host(host: str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        sanitized_host = subprocess.quote(host)
        args = ['ping', sanitized_host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}