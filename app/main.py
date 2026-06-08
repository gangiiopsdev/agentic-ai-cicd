from fastapi import FastAPI
import subprocess
import shlex
import re
import asyncio

app = FastAPI()

async def _run_command(command: str, args: list) -> None:
    try:
        result = await asyncio.create_subprocess_exec(*shlex.split(command), *args,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            raise Exception(f'Command failed with error: {stderr.decode()}')
    except Exception as e:
        raise Exception(f'Command execution failed: {str(e)}')

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    await _run_command(f'ping {shlex.quote(host)}', [])
    return {'status': 'completed'}