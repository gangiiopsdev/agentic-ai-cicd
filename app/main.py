from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Ensure that host is a valid IP address or hostname
    if not validate_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'stdout': result.stdout.decode('utf-8'), 'stderr': result.stderr.decode('utf-8')}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

import re
def validate_host(hostname: str) -> bool:
    # Regular expression to validate IP address or hostname
    pattern = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^[a-zA-Z0-9]([-a-zA-Z0-9]*[a-zA-Z0-9])?$')
    return bool(pattern.match(hostname))