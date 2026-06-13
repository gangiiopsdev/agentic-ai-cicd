from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Removed the /home endpoint as it was not secure
    sanitized_host = sanitize_host(host)
    if len(sanitized_host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(shlex.split(f'ping {shlex.quote(sanitized_host)}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}