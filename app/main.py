from fastapi import FastAPI
import subprocess
import shlex
global allowlist
allowlist = ['ping']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in allowlist:
        raise ValueError('Invalid command')
    cmd = f'ping {shlex.quote(host)}'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'output': result.stdout.decode(), 'error': result.stderr.decode() if result.returncode != 0 else None}