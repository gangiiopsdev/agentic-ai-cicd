from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host name'}
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}