from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

async def secure_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::ffff:127.0.0.1']
    if host in allowed_hosts:
        safe_host = shlex.quote(host)
        args = ['ping', safe_host]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        stdout, stderr = process.communicate()

@app.get('/ping')
def ping(host: str):
    await secure_ping(host)
    return {'status': 'completed'}