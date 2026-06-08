from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_subprocess_call(args):
    # Use shlex to safely split command arguments
    try:
        args = shlex.split(' '.join(args))
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid input'}
    return safe_subprocess_call(['ping', host])