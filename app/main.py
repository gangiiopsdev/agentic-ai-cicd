from fastapi import FastAPI
import subprocess, shlex

async def ping(host):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    cmd = f'ping -c 4 {shlex.quote(host)}'
    args = shlex.split(cmd)
    try:
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}

app = FastAPI()
def is_valid_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    return await ping(host)