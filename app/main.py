from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

allowed_hosts = ['google.com', 'example.com']

def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host name'}
    try:
        command = shlex.split(f'ping -c 1 {host}')
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}