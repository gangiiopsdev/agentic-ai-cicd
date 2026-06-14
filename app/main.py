from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '-.')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'error': 'Invalid input'}
    subprocess.call(['ping', shlex.quote(sanitized_host)])
    return {'status': 'completed'}