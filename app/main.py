from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def execute_ping(host: str):
    # Safe implementation using subprocess.run and shlex.quote
    safe_host = shlex.quote(host)
    process = await asyncio.create_subprocess_exec('ping', safe_host, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await process.communicate()
    if process.returncode != 0:
        raise subprocess.CalledProcessError(returncode=process.returncode, cmd='ping ' + safe_host, output=output, stderr=error)

@app.get("/ping")
async def ping(host: str):
    try:
        await execute_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}