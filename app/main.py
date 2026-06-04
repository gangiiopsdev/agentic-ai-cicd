from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.', '_'))

async def run_ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = await asyncio.create_subprocess_exec('ping', sanitized_host, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': (await result.stdout.read()).decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': (await e.stderr.read()).decode('utf-8')}

@app.get('/ping')
def ping(host: str):
    return run_ping(host)