from fastapi import FastAPI
import subprocess
import re
import asyncio

async def safe_ping(host: str):
    try:
        # Validate host to ensure it's a valid IP address or hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host name')
        result = await asyncio.create_subprocess_exec('ping', '-c 1', subprocess.list2cmdline([host]), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    return await safe_ping(host)