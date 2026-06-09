from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def run_command(command):
    args = shlex.split(command)
    try:
        result = await asyncio.create_subprocess_exec(*args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    safe_host = shlex.quote(host)
    command = f'ping {safe_host}'
    return run_command(command)