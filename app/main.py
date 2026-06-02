from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return ''.join(c if c.isalnum() else '_' for c in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        escaped_host = escape_host(host)
        args = shlex.split(f'ping -c 1 {escaped_host} '
        subprocess.run(args, check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}