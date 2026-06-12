from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = {"example.com", "localhost"}
    return host in allowed_hosts

async def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    args = ['ping', shlex.quote(host)]
    process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await process.communicate()
    if error:
        return {"status": "error", "message": str(error)}
    else:
        return {"status": "completed", "output": output.decode()}