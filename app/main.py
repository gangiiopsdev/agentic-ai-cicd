from fastapi import FastAPI, HTTPException
import subprocess
import shlex
global app = FastAPI()

async def ping(host: str):
    try:
        # Validate the host to ensure it's safe for use in the shell command
        if not host.isalnum():
            raise ValueError('Invalid input')
        args = shlex.split(f'ping {shlex.quote(host)}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)