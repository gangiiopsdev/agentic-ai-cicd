from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping', host]
    if '/' in host or '\' in host:
        raise ValueError('Invalid host name')
    safe_args = [shlex.quote(arg) for arg in args]
    subprocess.run(safe_args, check=True)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Secure implementation
    safe_ping(host)
    return {'status': 'completed'}