from fastapi import FastAPI
import subprocess
from shlex import quote
from subprocess import Popen, PIPE

app = FastAPI()

def validate_host(host):
    # Implement host validation logic here
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400
    try:
        output, error = Popen(['ping', f'--{quote(host)}'], stdout=PIPE, stderr=PIPE, text=True).communicate()
        return {'output': output}, 200
    except Exception as e:
        return {'error': str(e)}, 500