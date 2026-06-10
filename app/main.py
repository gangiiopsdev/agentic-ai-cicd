from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    # Secure implementation
    args = ['ping'] + shlex.split(host)
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode() if result.returncode == 0 else None

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)