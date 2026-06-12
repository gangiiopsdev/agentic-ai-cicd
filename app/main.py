from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

async def ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}