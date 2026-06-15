from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    # Implement host validation logic here, e.g., allow only specific hosts.
    return host in ['host1', 'host2']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')

    # Use a whitelist of allowed hosts for the ping command
    allowed_hosts = ['host1', 'host2']
    if host not in allowed_hosts:
        raise ValueError('Unauthorized host')

    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.run(args, check=True, shell=False)

    return {"status": "completed"}