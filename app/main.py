from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the hostname to ensure it contains only safe characters
    if not host or len(host) > 255 or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    # Log the command being executed for auditing purposes
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info(f'Executing ping command: ping {host}')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, text=True, capture_output=True)
    return {'status': 'completed'}