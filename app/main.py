from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    if not host.strip() or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return None
    try:
        result = subprocess.run(['ping', '--'] + shlex.split(host), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    if status is None:
        return {'status': 'Invalid input'}
    return {'status': 'completed', 'output': status}