from fastapi import FastAPI
import subprocess
import shlex
cimport = 'ping'

app = FastAPI()

async def ping(host: str):
    try:
        # Use shlex.quote to escape any special characters in the host input
        output = await asyncio.create_subprocess_exec(cimport, shlex.quote(host), stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": (await output.communicate())[0].decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)