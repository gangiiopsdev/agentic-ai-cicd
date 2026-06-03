from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Use shlex.quote to safely quote the host parameter
        result = subprocess.run(['ping', '-c', '1'] + [shlex.quote(arg) for arg in shlex.split(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)