from fastapi import FastAPI
import os
import shlex

app = FastAPI()

async def ping(host: str):
    try:
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}