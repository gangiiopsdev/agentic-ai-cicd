from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

async def run_ping(host):
    try:
        result = await asyncio.create_subprocess_exec('ping', quote(host), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return run_ping(host)