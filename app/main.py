from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    import re
    return re.match(r'^[a-zA-Z0-9.-]+$', host) and any(c.isdigit() for c in host)

def execute_ping_command(host):
    if not is_valid_host(host):
        raise ValueError('Invalid input')
    command = ['ping', host]
    subprocess.run(command, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    execute_ping_command(host)
    return {'status': 'completed'}