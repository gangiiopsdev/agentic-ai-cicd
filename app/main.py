from fastapi import FastAPI
import subprocess
import asyncio

global app
app = FastAPI()

async def ping(host: str):
    # Safe implementation
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True)
        return {'result': 'Success'}
    except subprocess.CalledProcessError as e:
        return {'result': 'Failure', 'error': e.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)