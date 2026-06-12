from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    try:
        output = await asyncio.create_subprocess_exec('ping', *shlex.split(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = await output.communicate()
        return {'stdout': result[0].decode(), 'stderr': result[1].decode()}
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    result = await safe_ping(host)
    return {"status": "completed", "output": result}

import re
def validate_host(host):
    # Simple regex to allow only alphanumeric characters and hyphens
    pattern = r'^[a-zA-Z0-9-]+$'
    return re.match(pattern, host) is not None