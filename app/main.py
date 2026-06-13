from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    args = shlex.split(f'ping {host}')
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()

@app.get('/ping')
def ping(host: str):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, safe_ping, host)
    return {'status': 'completed'}