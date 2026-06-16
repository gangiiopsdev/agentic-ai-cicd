from fastapi import FastAPI
import re
import subprocess

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    args = ['ping', '-c', '1'] + [host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

def safe_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'message': 'Ping failed', 'error': e.stderr}