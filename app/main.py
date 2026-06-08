from fastapi import FastAPI
import subprocess
import shlex

def is_valid_host(host):
    import re
    return re.match(r'^[a-zA-Z0-9.-]+$', host) and any(c.isdigit() for c in host)

def execute_ping_command(host):
    if not is_valid_host(host):
        raise ValueError('Invalid input')
    command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(command, check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())
        return False
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if execute_ping_command(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}