from fastapi import FastAPI
import asyncio
import re

app = FastAPI()

async def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        return {'status': 'error', 'error': 'Invalid input'}

    command = f'ping {shlex.quote(host)}'
    result = await asyncio.create_subprocess_exec('sh', '-c', command, stderr=subprocess.PIPE)
    output, _ = await result.communicate()
    return {'status': 'completed', 'result': output.decode('utf-8')}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)