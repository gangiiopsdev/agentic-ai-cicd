from fastapi import FastAPI
import subprocess
from shlex import quote
from subprocess import run, PIPE

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    result = run(['ping', '-c', '1', quote(host)], stdout=PIPE, stderr=PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode('utf-8'), 'stderr': result.stderr.decode('utf-8')}