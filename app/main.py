from fastapi import FastAPI
import subprocess
import re
def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    args = ['ping', '-c', '1'] + [host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
def safe_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if safe_ping(host) is False:
        return {'status': 'failed'}
    else:
        return {'status': 'completed'}