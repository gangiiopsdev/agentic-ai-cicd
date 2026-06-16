from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_hosts = ['127.0.0.1', '::1']  # List of allowed hosts
    if host not in safe_hosts:
        return {'error': 'Invalid host'}
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}

# No need for '/ping_safe' if only using it to restrict hosts