from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    # Basic sanitization: only allow alphanumeric characters and some punctuation
    return ''.join(c for c in host if c.isalnum() or c in '-.:/')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.call(args)
    return {'status': 'completed'}