from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def run_ping(host: str):
    # Validate the input to ensure it does not contain potentially dangerous characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid input'
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        stdout, stderr = await result.communicate()
        if result.returncode == 0:
            return stdout
        else:
            return f'Ping failed with error: {stderr}''
    except Exception as e:
        return f'An error occurred: {e}''

@app.get("/ping")
def ping(host: str):
    return run_ping(host)