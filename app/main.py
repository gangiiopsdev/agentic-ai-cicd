from fastapi import FastAPI
import subprocess
import shlex
from shlex import quote as cmd_quote

app = FastAPI()

def validate_host(host):
    # Basic validation logic for host
    if 'localhost' not in host and '@' not in host:
        raise ValueError('Invalid host input')

@app.get('/ping')
def ping(host: str):  
    try:
        validate_host(host)
        result = subprocess.run(shlex.split(f'ping {cmd_quote(host)}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}