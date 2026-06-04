from fastapi import FastAPI
import subprocess
import re

async def safe_ping(host: str):
    # Basic validation of host
    if not re.match(r'^[a-zA-Z0-9.-]*$', host):
        return 'Invalid host'
    args = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return result.stdout

global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = await safe_ping(host)
    return {'status': 'completed', 'output': output}