from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate or sanitize the host parameter to prevent command injection
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}
    result = getattr(subprocess, 'run', getattr(subprocess, '_run', getattr(subprocess, '_old_run')))(f'ping {host}', capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}