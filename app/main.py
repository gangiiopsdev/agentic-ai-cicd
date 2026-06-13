from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

async def run_ping(request: PingRequest):
    try:
        safe_host = shlex.quote(request.host)
        result = await asyncio.to_thread(subprocess.run, ['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.post("/ping")
async def ping(request: PingRequest):
    return await run_ping(request)