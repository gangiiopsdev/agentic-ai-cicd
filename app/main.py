from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    if not host or len(host) > 255:
        raise ValueError('Invalid host parameter')
    return host.replace(';', '').replace('&', '').replace('|', '')

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            raise ValueError('Invalid host parameter')
    return host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validated_host = validate_host(host)
    args = ['ping'] + shlex.split(validated_host)
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}