from fastapi import FastAPI
import subprocess
import shlex

async def ping(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            raise ValueError('Invalid host name')
    args = ['ping', shlex.quote(host)]  # Use shlex.quote to safely include the host in the command
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    try:
        output = await ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}