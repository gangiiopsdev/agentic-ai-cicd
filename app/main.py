from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def run_ping(host: str):
    if not re.match(r'^\d+$', host):  # Validate input using regular expression
        return 'Invalid host'
    args = ['ping', '-c', '1', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get('/ping')
def ping(host: str):
    if not re.match(r'^\d+$', host):  # Validate input using regular expression
        return {'status': 'error', 'message': 'Invalid host'}
    output = run_ping(host)
    return {'status': 'completed', 'output': output}