from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host):
    if not re.match(r'^[a-zA-Z0-9]{1,64}$', host):
        raise ValueError('Invalid hostname')
    return host

@app.get('/ping')
def ping(host: str):
    host = sanitize_host(host)
    args = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}