from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def ping(host: str):
    # Validate host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or '.' not in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            return {'status': 'failed', 'error': result.stderr}
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}