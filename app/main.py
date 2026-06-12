from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced validation to prevent command injection
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = ['ping', '--'] + [host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex to allow only valid IP addresses or domain names
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None