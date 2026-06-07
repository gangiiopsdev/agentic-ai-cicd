from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    # Define a list of safe hosts or patterns
    safe_hosts = ['example.com', 'localhost']
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        return {'error': 'Invalid host'}, 400
    if not is_safe_host(host):
        return {'error': 'Host is not allowed'}, 403
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}