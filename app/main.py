from fastapi import FastAPI
import subprocess
import shlex

async def ping(host: str):
    # Secure implementation with input validation and quoting
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host')
    sanitized_host = shlex.quote(host)
    await asyncio.create_subprocess_exec('ping', '-c', '1', sanitized_host, check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)