from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

async def secure_ping(host: str):
    if not host or len(host.strip()) == 0:
        raise ValueError('Invalid command')
    # Use os.path.realpath to ensure the path is canonical and safe
    safe_host = os.path.realpath(host)
    command = ['ping', *shlex.split(safe_host)]
    result = await asyncio.to_thread(subprocess.run, command, check=True, shell=False, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)