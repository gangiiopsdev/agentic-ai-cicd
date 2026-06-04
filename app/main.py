from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    if is_safe_host(host):
        return ping(host)
    else:
        return {'status': 'error', 'output': 'Invalid host'}

def is_safe_host(host: str):
    # Add logic to validate and sanitize the host input
    allowed_hosts = ['192.168.1.1', '10.0.0.1']  # Example list of safe hosts
    return host in allowed_hosts