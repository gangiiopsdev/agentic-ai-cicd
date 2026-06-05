from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def run_ping(host: str):
    try:
        # Validate host input to ensure it does not contain malicious content
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host input')
        result = await asyncio.subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
        return result.stdout
    except (subprocess.CalledProcessError, ValueError) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = await run_ping(host)
    return {'status': 'completed', 'response': response}