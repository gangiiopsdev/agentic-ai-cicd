from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    result = await asyncio.create_subprocess_exec('ping', shlex.quote(host), stdout=subprocess.PIPE)
    output, _ = await result.communicate()
    return {'status': 'completed', 'output': output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)