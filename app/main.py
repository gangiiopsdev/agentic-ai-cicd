from fastapi import FastAPI
import subprocess
import shlex
import os

async def secure_ping(host: str):
    escaped_host = shlex.quote(host)
    command = ['ping', '-c', '1', escaped_host]
    result = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await result.communicate()
    return stdout, stderr

def home(request):
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        stdout, stderr = secure_ping(host)
        if stderr:
            raise Exception(stderr.decode())
        return {'status': 'completed', 'output': stdout.decode()}
    except Exception as e:
        return {'error': str(e)}