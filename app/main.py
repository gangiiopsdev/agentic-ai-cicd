from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced implementation with input validation and shlex.quote
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}