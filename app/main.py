from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

async def run_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode == 0:
            return {'status': 'completed', 'output': output.decode('utf-8')}
        else:
            return {'status': 'failed', 'error': error.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

async def sanitize_host(host: str):
    # Add additional sanitization logic here if needed
    return host

@app.get('/ping')
async def ping(host: str):
    sanitized_host = await sanitize_host(host)
    return await run_ping(sanitized_host)