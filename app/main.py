from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

async def ping(host: str):
    if not is_safe_host(host):
        return {"status": "error", "message": "Invalid host"}
    args = ['ping', shlex.quote(host)]
    process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await process.communicate()
    if error:
        return {"status": "error", "message": str(error)}
    else:
        return {"status": "completed", "output": output.decode()}

async def is_safe_host(host: str):
    # Implement logic to check if the host is safe to ping
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts