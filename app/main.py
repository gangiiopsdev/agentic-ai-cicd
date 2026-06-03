from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def ping(host: str):
    # Validate host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host format'}

    try:
        output = subprocess.run(['ping', '-c', '1', '--'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}