from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if not host or len(host) > 255 or not host.replace('.', '', 3).isdigit():
        return {'status': 'failed', 'error': 'Invalid host'}
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(shlex.split(f'ping {safe_host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}