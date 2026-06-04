from fastapi import FastAPI
import subprocess
import shlex
import re
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c.isdigit())
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Validate the hostname to allow only alphanumeric characters and digits
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        return {'status': 'error', 'output': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping'] + shlex.split(host), check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}