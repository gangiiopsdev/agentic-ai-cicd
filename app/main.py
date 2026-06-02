from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host not in allowed_hosts:
        return {'status': 'denied'}
    args = shlex.split(f'ping -c 4 {host}')
    process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await process.communicate()
    if error:
        return {'status': 'error', 'message': error.decode()}
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    if host not in ['8.8.8.8', '127.0.0.1']:
        return {'status': 'denied'}
    args = shlex.split(f'ping -c 4 {host}')
    process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await process.communicate()
    if error:
        return {'status': 'error', 'message': error.decode()}
    return {'status': 'completed'}