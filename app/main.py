from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

async def safe_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ['.', '-', '_'])

@app.get("/ping")
def ping(host: str):
    safe_host_value = await safe_host(host)
    command = f'ping {shlex.quote(safe_host_value)}'
    process = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        raise Exception(error.decode('utf-8'))
    return {'status': 'completed', 'output': output.decode('utf-8')}