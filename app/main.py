from fastapi import FastAPI
import asyncio
from pydantic import BaseModel
import re

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., check if the host is within a whitelist
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

async def run_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.post("/ping")
def ping(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}

    # Sanitize the host input before using it in subprocess
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', request.host)
    return await run_ping(sanitized_host)