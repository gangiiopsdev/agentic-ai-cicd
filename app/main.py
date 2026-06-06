from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'error': 'Invalid input'}

    command = shlex.split(f'ping {host}')
    result = await asyncio.create_subprocess_exec(*command, stderr=subprocess.PIPE)
    output, _ = await result.communicate()
    return {'status': 'completed', 'result': output.decode('utf-8')}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)