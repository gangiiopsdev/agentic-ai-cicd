from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

allowed_hosts = re.compile(r'^[a-zA-Z0-9.-]+$')

@app.get('/ping')
def ping(host: str):
    if not allowed_hosts.match(host):
        return {'error': 'Invalid host name'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}