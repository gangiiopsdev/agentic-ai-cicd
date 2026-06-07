from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def execute_ping(host: str):
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid input for host')

@app.get('/ping')
def ping(host: str):
    try:
        result = execute_ping(host)
        return {'result': result}
    except Exception as e:
        return {'error': str(e)}