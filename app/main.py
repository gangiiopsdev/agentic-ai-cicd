from fastapi import FastAPI
import subprocess
from shlex import quote

allowed_hosts = ['example.com', 'test.com']

def validate_host(host):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

async def safe_subprocess_call(command, *args, **kwargs):
    import shlex
    command = shlex.split(command)
    subprocess.call(['ping', quote(sanitize_input(command))], *args, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    safe_subprocess_call(f'ping {host}')
    return {"status": "completed"}