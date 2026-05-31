from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

async def ping(host: str):
    try:
        args = ['ping', host]  # Directly use the host without shell=True and shlex.split
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)