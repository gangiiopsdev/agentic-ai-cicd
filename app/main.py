from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_safe_hostname(hostname):
    return all(c.isalnum() or c in '-.' for c in hostname)

def escape_shell_arg(arg):
    if not arg:
        return ''
    arg = shlex.quote(arg)
    return f"'{arg}'"

@app.get('/ping')
def ping(host: str):
    if not host.strip() or not is_safe_hostname(host):
        return {'error': 'Invalid host name'}
    try:
        subprocess.run(shlex.split(f'ping {escape_shell_arg(host)}'), check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}