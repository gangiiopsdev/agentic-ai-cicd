from fastapi import FastAPI
import subprocess
import shlex
import re
global app = FastAPI()

async def ping(host: str):
    # Validate input to ensure it only contains alphanumeric characters and hyphens
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        raise ValueError('Invalid input')
    # Sanitize input by escaping special characters
    host = shlex.quote(host)
    args = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)