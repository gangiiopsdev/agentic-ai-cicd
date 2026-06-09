from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str

async def safe_ping(host: str) -> str:
    result = await asyncio.create_subprocess_exec('ping', host, stdout=asyncio.subprocess.PIPE)
    stdout, stderr = await result.communicate()
    return stdout.decode()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    output = safe_ping(request.host)
    return {'status': 'completed', 'output': output}