from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def safe_ping(host: str):
    if not host.isnumeric():
        return False
    args = shlex.split('ping ' + host)
    try:
        await asyncio.create_subprocess_exec(*args, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "reason": "Invalid host"}