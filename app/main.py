from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    safe_host = escape_shell_arg(host)
    args = shlex.split(f'ping {safe_host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}