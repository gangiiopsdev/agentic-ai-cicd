from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate the host input to ensure it's safe
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

    # Secure implementation using subprocess.run with proper error handling and shlex for safe argument splitting
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)