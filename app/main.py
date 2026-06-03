from fastapi import FastAPI, HTTPException
import subprocess
import shlex
import re

app = FastAPI()

async def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        raise HTTPException(status_code=422, detail='Invalid input')
    try:
        args = ['ping', '-c', '1', shlex.quote(host)]
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)