from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safe implementation using shlex.quote to prevent shell injection
    args = ['ping', shlex.quote(host)]
    process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE)
    output, _ = await process.communicate()
    return output.decode()

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)