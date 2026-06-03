from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

async def run_ping(host: str):
    try:
        # Use subprocess.run with shell=False and sanitized input
        result = await asyncio.create_subprocess_exec('ping', host, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': (await result.stdout.read()).decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': (await e.stderr.read()).decode('utf-8')}

@app.get('/ping')
async def ping(host: str):
    return await run_ping(host)