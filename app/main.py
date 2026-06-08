from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

async def ping(host: str):
    if is_valid_host(host.strip()):
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return output.decode('utf-8'), error.decode('utf-8') if error else None
    else:
        return None

@app.get("/ping")
def get_ping_status():
    return {"status": "completed"}