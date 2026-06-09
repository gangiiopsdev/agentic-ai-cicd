from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts and re.match(r'^[a-fA-F0-9:.]+$', host):
        args = ['ping', host]
        # Use asyncio to run the ping command asynchronously
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}