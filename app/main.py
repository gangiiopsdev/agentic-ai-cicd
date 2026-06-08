from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and sanitized input
    try:
        cmd = ['ping'] + shlex.split(host)
        result = await asyncio.create_subprocess_exec(*cmd, capture_output=True, text=True, check=True)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return {'status': 'invalid', 'message': 'Invalid input'}
    return await ping(host)