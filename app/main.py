from fastapi import FastAPI
import asyncio
import re

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    try:
        result = await asyncio.create_subprocess_exec(*args, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)