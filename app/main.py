from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

def validate_host(host):
    if not all(char.isalnum() or char in '-.' for char in host):
        raise ValueError('Invalid characters in host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        sanitized_host = sanitize_host(host)
        args = ['ping', *shlex.split(sanitized_host)]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except (ValueError, subprocess.CalledProcessError) as e:
        return {'status': 'failed', 'error': str(e)}