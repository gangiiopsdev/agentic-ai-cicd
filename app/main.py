from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

def is_valid_host(host):
    # Regex to validate hostnames or IP addresses
    pattern = re.compile(r'^([a-zA-Z0-9.-]+|localhost|127.0.0.1)$')
    if not pattern.match(host):
        return False
    return True