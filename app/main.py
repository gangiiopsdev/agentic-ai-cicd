from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

async def ping(host: str):
    try:
        # Validate the host input to ensure it only contains alphanumeric characters and hyphens
        if not host.replace('-', '').isalnum():
            raise ValueError('Invalid input')
        args = shlex.split(f'ping {host}')  # Safely parse the host input as part of a command
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)