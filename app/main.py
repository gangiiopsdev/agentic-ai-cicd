from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def is_safe_host(host):
    return host.isalnum() and '-' not in host

@app.get('/ping')
def ping(host: str):
    if not await is_safe_host(host):
        return {'error': 'Invalid input'}, 400
    safe_command = ['ping', '127.0.0.1', host]
    subprocess.call(safe_command, shell=False)
    return {'status': 'completed'}