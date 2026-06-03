from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def safe_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ['.', '-', '_'])

@app.get("/ping")
def ping(host: str):
    safe_host_value = await safe_host(host)
    command = 'ping' + ' ' + shlex.quote(safe_host_value)
    subprocess.run(command, shell=False, check=True)
    return {"status": "completed"}