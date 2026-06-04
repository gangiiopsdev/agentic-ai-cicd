from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def safe_ping(host):
    # Regular expression to validate hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'stderr': 'Invalid hostname'}
    command = shlex.split(f'ping -c 1 {host}')
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)