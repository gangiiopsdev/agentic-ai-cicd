from fastapi import FastAPI
import os
import re
import shlex

app = FastAPI()

async def safe_ping(host: str):
    try:
        output = await asyncio.subprocess.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = await output.wait()
        return output.stdout.decode('utf-8')
    except (subprocess.CalledProcessError, TimeoutExpired) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid hostname'}
    # Sanitize the input to prevent shell injection
    sanitized_host = shlex.quote(host)
    return {'status': await safe_ping(sanitized_host)}