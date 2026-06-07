from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

async def safe_ping(host: str):
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await result.communicate()
    return stdout.decode(), stderr.decode()

def ping(host: str):
    try:
        output, error = safe_ping(host)
        if error:
            return {'status': 'failed', 'error': error}
        else:
            return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(request: PingRequest):
    if not request.host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(request.host)