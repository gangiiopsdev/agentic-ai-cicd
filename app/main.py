from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        # Using shlex.split to safely split the command into a list of arguments
        subprocess.run(shlex.split(f'ping {host}'), check=True)
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}