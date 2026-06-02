from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

async def execute_safe_command(command, *args):
    try:
        result = await asyncio.create_subprocess_exec(*[command] + [shlex.quote(arg) for arg in args], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

def ping(host: str):
    # Secure implementation using subprocess.run with check=True and shell=False
    result = execute_safe_command('ping', host)
    return result