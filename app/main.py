from fastapi import FastAPI
import re
import shlex

app = FastAPI()

async def ping(host: str):
    # Ensure host contains only allowed characters to prevent shell injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = await asyncio.create_subprocess_exec('ping', *shlex.split(host), stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            raise subprocess.CalledProcessError(returncode=output.returncode, cmd='ping', output=stderr.decode())
        return {'status': 'completed', 'output': stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}