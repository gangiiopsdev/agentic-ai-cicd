from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.strip():
        raise ValueError('Host parameter cannot be empty or whitespace only.')
    ping_command = ['ping', shlex.quote(host)]
    subprocess.run(ping_command, check=True)
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}