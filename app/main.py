from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '._-')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = shlex.split(f'ping --no-host-alias --non-privileged {shlex.quote(sanitized_host)}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}