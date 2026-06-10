from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional
import asyncio

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def safe_ping(host: str) -> str:
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=asyncio.subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode()
    except Exception as e:
        return f'Error: {e}'

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    output = safe_ping(request.host)
    return {'status': 'completed', 'output': output}