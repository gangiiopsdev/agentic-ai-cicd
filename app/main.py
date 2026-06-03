from fastapi import FastAPI
import subprocess
import shlex

async def ping(host: str):
    # Validate the input to prevent command injection
    try:
        args = shlex.split('ping ' + host)
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output}
    except (subprocess.CalledProcessError, asyncio.TimeoutError) as e:
        return {'status': 'failed', 'error': str(e)}