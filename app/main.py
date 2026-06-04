from fastapi import FastAPI
import subprocess

async def ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}