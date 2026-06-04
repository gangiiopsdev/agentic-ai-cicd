from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):  # Validate the host input to prevent injection attacks
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1', host]  # Limit the number of pings and use -c for compatibility
    subprocess.run(args, check=True)
    return {'status': 'completed'}