from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        args = shlex.split(f'ping {shlex.quote(host)}')  # Use f-string and shlex.quote for safer command construction
        result = subprocess.run(['ping'] + args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_endpoint(host: str):
    return await ping(host)