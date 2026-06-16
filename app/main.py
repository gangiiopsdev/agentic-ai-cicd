from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}