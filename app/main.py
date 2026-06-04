from fastapi import FastAPI
import subprocess
import re
import shlex

async def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "output": "Invalid hostname"}
    result = await asyncio.create_subprocess_exec('ping', '-c', '1', shlex.quote(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    if result.returncode != 0:
        return {"status": "failed", "output": error.decode()}
    return {"status": "completed", "output": output.decode()}

app = FastAPI()

@app.get('/ping')
async def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "output": "Invalid hostname"}
    result = await asyncio.create_subprocess_exec('ping', '-c', '1', shlex.quote(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    if result.returncode != 0:
        return {"status": "failed", "output": error.decode()}
    return {"status": "completed", "output": output.decode()}