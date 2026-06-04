from fastapi import FastAPI
import subprocess
import re
import shlex

async def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "output": "Invalid hostname"}
    result = await asyncio.to_thread(subprocess.run, ['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "output": "Invalid hostname"}
    result = await asyncio.to_thread(subprocess.run, ['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}