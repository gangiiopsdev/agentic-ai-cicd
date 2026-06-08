from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    if not host or len(host) > 255 or '.' not in host:
        raise ValueError('Invalid host input')
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Host contains invalid characters')
    return shlex.quote(host)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', '-c', '1', '--', sanitized_host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': str(e)}