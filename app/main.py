from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(host):
    return ''.join(c for c in host if c.isalnum() or c in ['.', '-', '_'])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(shlex.split(f'ping {sanitized_host}'), capture_output=True, text=True)
    return {'status': result.stdout}