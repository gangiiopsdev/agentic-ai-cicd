from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'invalid_host'}
    args = shlex.split('ping ' + host)
    subprocess.call(args)
    return {'status': 'completed'}