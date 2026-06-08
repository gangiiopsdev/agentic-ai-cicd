from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(host):
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host input')
    return host

app = FastAPI()

@app.post('/ping/')
def ping_host(host: str):
    try:
        cmd = ['ping', shlex.quote(sanitize_input(host))]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}