from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host: str) -> str:
    if '.' not in host and '@' not in host:
        return None
    return host

cmd_template = ['ping', '-c 1']

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is None:
        return {'status': 'failed', 'error': 'Invalid host'}
    result = subprocess.run(cmd_template + shlex.split(shlex.quote(sanitized_host)), check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}