from fastapi import FastAPI
import shlex
from sanic.response import json

app = FastAPI()

async def execute_safe_ping(host: str):
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping'] + shlex.split(host)
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    output = result.stdout
    if result.stderr:
        output += '\n' + result.stderr
    return {'status': 'completed', 'output': output}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return execute_safe_ping(host)