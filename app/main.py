from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if host.isnumeric():
        command = ['ping', '-c', '1', shlex.quote(host)]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'stdout': result.stdout, 'stderr': result.stderr}
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isnumeric():
        return {'error': 'Invalid host'}
    try:
        result = safe_ping(host)
        return {'status': result}
    except ValueError as e:
        return {'error': str(e)}