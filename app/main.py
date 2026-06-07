from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    return {'status': 'completed', 'output': output.decode('utf-8'), 'error': error.decode('utf-8')}