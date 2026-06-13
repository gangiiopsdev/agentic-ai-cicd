from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get('/ping')
async def ping(host: str):
    if not await is_safe_host(host):
        raise ValueError('Invalid host')
    cmd = ['ping', shlex.quote(host)]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed', 'output': output.decode() if not error else error.decode()}