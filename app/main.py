from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid input')

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        command = ['ping', shlex.quote(host)]
        subprocess.run(command, check=True)
        return {'status': 'completed'}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}