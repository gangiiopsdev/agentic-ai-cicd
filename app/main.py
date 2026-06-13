from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    try:
        command = ['ping', host]
        output = await asyncio.create_subprocess_exec(*command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        return await output.stdout.read()
    except Exception as e:
        return f'Ping failed: {e.stderr.read() if e.stderr else str(e)}'

@app.get("/ping")
async def ping(host: str):
    return await safe_ping(shlex.quote(host))