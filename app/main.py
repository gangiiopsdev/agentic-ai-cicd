from fastapi import FastAPI
import subprocess
import shlex
import asyncio

async def safe_ping(host):
    if not host.isdigit():
        return "Invalid host"
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        result = await asyncio.create_subprocess_exec(*args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'success', 'output': (await result.stdout.read()).decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': (await e.stderr.read()).decode()}

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(shlex.quote(host))