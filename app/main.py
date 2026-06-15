from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    # Secure implementation using shlex for argument parsing
    try:
        args = shlex.split(f'ping {host}')
        result = await asyncio.create_subprocess_exec(*args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'success', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)