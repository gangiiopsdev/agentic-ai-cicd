from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_safe_hostname(hostname):
    # Implement a more robust hostname validation logic here
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(hostname)) and hostname == 'example.com'

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {'status': 'failed', 'error': 'Unsafe host'}
    try:
        cmd = ['ping'] + shlex.split(host)
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}