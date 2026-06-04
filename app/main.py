from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Validate the host input using a simple regex pattern that allows only alphanumeric characters and dots
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        args = ['ping', '-c', '4', host]  # Limiting the number of pings to 4
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result
    else:
        return {'status': 'completed'}