from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Validate host input before processing
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        raise ValueError('Invalid host name')

    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}