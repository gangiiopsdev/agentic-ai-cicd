from fastapi import FastAPI, HTTPException
import subprocess
import shlex
global app = FastAPI()

async def ping(host: str):
    try:
        # Use a whitelist of allowed hosts or validate the input more strictly
        if host not in ['example.com', 'test.com']:
            raise ValueError('Invalid host')
        args = shlex.split(f'ping {shlex.quote(host)}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)

@app.get("/ping")
def ping_route(host: str):
    try:
        # Use a more robust validation method to prevent command injection
        if not (host.isalnum() and '.' in host and '/' not in host):
            raise ValueError('Invalid input')
        return await ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}