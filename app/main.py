from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def is_valid_host(host):
    return bool(re.match(r'^[a-zA-Z0-9.-]+$', host))

def escape_host(host):
    return shlex.quote(host)

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        args = ['ping', escape_host(host)]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}