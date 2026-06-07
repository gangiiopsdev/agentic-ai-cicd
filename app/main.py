from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f'ping {host}')
        await asyncio.create_subprocess_exec(*args)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}