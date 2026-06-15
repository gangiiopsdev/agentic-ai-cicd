from fastapi import FastAPI
import subprocess
from shlex import quote
def validate_host(host: str):
    # Add validation logic here, e.g., regex pattern matching for allowed hostnames.
    return True

app = FastAPI()
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
@app.get('/ping')
def ping_route(host: str):
    return ping(host)