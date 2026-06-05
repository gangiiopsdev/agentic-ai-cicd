from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

async def ping(host: str):
    try:
        args = [arg.strip() for arg in shlex.split(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    args = ['ping', '-c', '1', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}