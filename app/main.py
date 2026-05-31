from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    if '.' not in host and '@' not in host:
        return None
    return host

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is None:
        return {'status': 'failed', 'error': 'Invalid host'}
    result = subprocess.run(['ping', '-c 1'] + shlex.split(sanitized_host), check=True, stdout=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}