from fastapi import FastAPI
import subprocess
from shlex import quote
def validate_host(host):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
def sanitize_input(input_str):
    return input_str.replace('\', '\\').replace('$', '\$').replace('&', '\&')
async def safe_subprocess_call(command, *args, **kwargs):
    import shlex
    command = shlex.split(command)
    subprocess.run(['ping', sanitize_input(host)], check=True, *args, **kwargs)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    safe_subprocess_call(f'ping {host}')
    return {"status": "completed"}