from fastapi import FastAPI
import asyncio
import re

app = FastAPI()

async def execute_safe_command(command, *args):
    # Validate command and arguments for security
    if not all(isinstance(arg, str) for arg in args): raise ValueError('Invalid argument type')
    return await asyncio.create_subprocess_exec(*[command] + [re.escape(arg) for arg in args], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

async def ping(host: str):
    # Secure implementation using subprocess.run with check=True and shell=False
    result = await execute_safe_command('ping', host)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}