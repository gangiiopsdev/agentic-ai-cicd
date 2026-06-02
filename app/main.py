from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host: str):
    # Validate the host to ensure it's a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')

    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            return f'Ping failed: {stderr.decode()}'
        return stdout.decode()
    except Exception as e:
        return f'Ping failed: {str(e)}'

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}