from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
from typing import Union

app = FastAPI()

async def safe_ping(host: str) -> Union[str, None]:
    # Validate the input host to prevent command injection
    if not is_safe_host(host):
        return None
    try:
        result = await subprocess.run(['ping', cmd_quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)

async def is_safe_host(host: str) -> bool:
    # Add logic to validate the host input
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example allowed hosts
    return host in allowed_hosts