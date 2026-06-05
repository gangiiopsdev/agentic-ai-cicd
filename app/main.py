from fastapi import FastAPI
import subprocess
import re
import shlex
def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9]{1,64}$', host):
        raise ValueError('Invalid input for host')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), check=True, capture_output=True, text=True)
    except Exception as e:
        return {'error': str(e)}
    return {'status': 'completed'}