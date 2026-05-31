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

def validate_host(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')

@app.get("/ping")
def ping_route(host: str):
    try:
        validate_host(host)
        return await ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}