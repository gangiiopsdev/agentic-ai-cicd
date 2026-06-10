from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def safe_ping(host: str):
    try:
        # Validate the host input to ensure it is a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host input')
        output = await asyncio.create_subprocess_exec('ping', shlex.quote(host), stderr=subprocess.STDOUT, timeout=5)
        result = await output.wait()
        return {'status': 'completed', 'output': (await output.stdout.read()).decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
async def ping(host: str):
    try:
        # Validate the host input to ensure it is a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host input')
        return await safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}