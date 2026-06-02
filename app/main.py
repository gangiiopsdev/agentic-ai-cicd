from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

def execute_safe_command(command, *args):
    return await asyncio.create_subprocess_exec(*[command] + [shlex.quote(arg) for arg in args], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

async def ping(host: str):
    result = await execute_safe_command('ping', host)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}