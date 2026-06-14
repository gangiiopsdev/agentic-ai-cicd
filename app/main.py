from fastapi import FastAPI
import shlex
import re

async def safe_ping(host):
    # Validate and sanitize host input
    if not host.strip() or host.strip().endswith(' '):
        raise ValueError('Invalid host value')
    # Use regular expression to ensure the host is a valid hostname/IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host value')
    args = ['ping', shlex.quote(host)]
    result = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await result.communicate()
    return stdout.decode().strip()
class FastAPISafePing(FastAPI):
    @app.get("/ping")
    async def ping(self, host: str):
        output = await safe_ping(host)
        return {"status": "completed", "output": output}

app = FastAPISafePing()