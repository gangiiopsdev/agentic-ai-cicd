from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host.strip() or '..' in sanitized_host.split('/'):
        return {'error': 'Invalid host'}, 400
    args = ['ping', *shlex.split(sanitized_host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}