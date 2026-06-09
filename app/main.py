from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    try:
        output = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}