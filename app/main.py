from fastapi import FastAPI
import asyncio
import re
import shlex
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '-.').strip()

async def execute_ping(host):
    # Validate and sanitize host input
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError('Invalid hostname')
    try:
        cmd = ['ping', shlex.quote(sanitized_host)]
        output = await asyncio.create_subprocess_exec(*cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        return {'status': 'completed', 'output': stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return await execute_ping(host)