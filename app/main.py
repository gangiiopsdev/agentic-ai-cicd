from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_command(args):
    return [quote(arg) for arg in args]
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not host.isalnum() and '-' not in host and '_' not in host and '.' not in host:
        return {'error': 'Invalid host'}
    subprocess.run(safe_command(['ping', quote(host)]), check=True)
    return {'status': 'completed'}