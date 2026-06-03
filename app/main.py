from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['example.com']  # Define allowed hosts
    if host in allowed_hosts:
        try:
            args = shlex.split(f'ping -c 1 {host}')
            output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)