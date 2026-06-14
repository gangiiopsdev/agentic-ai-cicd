from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['127.0.0.1', '::1']  # List of allowed hosts
    return host in safe_hosts

async def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command_parts = ['ping', *shlex.split(host)]
    result = await asyncio.create_subprocess_exec(*command_parts, check=True)
    return {'status': 'completed', 'output': result}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command_parts = ['ping', *shlex.split(host)]
    result = await asyncio.create_subprocess_exec(*command_parts, check=True)
    return {'status': 'completed', 'output': result}