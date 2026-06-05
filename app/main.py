from fastapi import FastAPI
import subprocess
def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
def safe_ping(hostname: str):
    # Use shlex.quote to safely handle command arguments
    command = ['ping', '-c', '1', shlex.quote(hostname)]
    subprocess.run(command, check=True)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    validate_host(host)
    safe_ping(host)
    return {'status': 'completed'}