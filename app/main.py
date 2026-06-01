from fastapi import FastAPI, HTTPException
import subprocess
import shlex

class PingInputValidator:
    ALLOWED_HOSTS = ['example.com', 'test.com']

    @staticmethod
def is_valid_host(host: str) -> bool:
        return host in cls.ALLOWED_HOSTS

app = FastAPI()

async def ping(host: str):
    if not PingInputValidator.is_valid_host(host):
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {shlex.quote(host)}')
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)