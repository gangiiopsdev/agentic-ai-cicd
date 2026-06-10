from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    command_parts = ['ping', shlex.quote(host)]  # Use shlex.quote to safely include user input in the command
    result = await asyncio.to_thread(subprocess.run, command_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}