from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', cmd_quote(host)], check=True)
    return {'status': 'completed'}