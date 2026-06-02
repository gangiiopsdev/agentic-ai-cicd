from fastapi import FastAPI
import subprocess

async def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host name'}

    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output}
    except (subprocess.CalledProcessError, asyncio.TimeoutError) as e:
        return {'status': 'failed', 'error': str(e)}