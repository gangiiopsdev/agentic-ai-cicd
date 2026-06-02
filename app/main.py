from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate input to ensure it's a valid hostname or IP address
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        raise ValueError('Invalid hostname or IP address')
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}