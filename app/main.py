from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    return sanitized_host
global_host_set = {'google.com', 'example.com'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host not in global_host_set:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', shlex.quote(sanitized_host)], check=True, shell=False)
    return {'status': 'completed'}