from fastapi import FastAPI
import subprocess
import shlex

global BLACKLISTED_HOSTS = ['example.com']

app = FastAPI()

async def safe_ping(host: str):
    if host in BLACKLISTED_HOSTS:
        raise ValueError('Unsafe host')
    cmd = ['ping', shlex.quote(host)]
    subprocess.call(cmd)

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed', 'result': safe_ping(host)}