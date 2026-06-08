from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate the host to ensure it does not contain malicious content
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host name')
    try:
        # Secure implementation using subprocess.run with proper shell=False and argument quoting
        subprocess.run(shlex.split(f'ping {host}'), check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f'Ping failed: {e}') from e

@app.get("/ping")
def ping_route(host: str):
    return ping(host)