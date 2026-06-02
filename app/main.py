from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

async def ping(request: PingRequest):
    validated_host = shlex.quote(request.host)
    result = await asyncio.create_subprocess_exec('ping', '-c', '1', validated_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await result.communicate()
    return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}

@app.get('/ping')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}