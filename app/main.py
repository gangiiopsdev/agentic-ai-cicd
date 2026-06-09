from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['192.168.1.1', '10.0.0.1']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        cmd = shlex.split(f'ping {host}')
        output = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}