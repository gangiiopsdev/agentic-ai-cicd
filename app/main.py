from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def safe_ping(host):
    try:
        # Validate host to ensure it's a valid IP address or hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host')
        output = await asyncio.create_subprocess_exec('ping', host, stderr=subprocess.STDOUT, timeout=5)
        stdout, stderr = await output.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    host = shlex.quote(host)
    return await safe_ping(host)