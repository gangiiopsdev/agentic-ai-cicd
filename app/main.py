from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

async def safe_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            raise Exception(stderr.decode('utf-8'))
        return {'status': 'completed', 'output': stdout.decode('utf-8')}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(request: PingRequest):
    return safe_ping(request.host)