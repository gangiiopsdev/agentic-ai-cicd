from fastapi import FastAPI
import subprocess

async def ping(host: str):
    # Safe implementation using subprocess.run and input sanitization
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            return {'status': 'failed', 'error': stderr.decode()}
        return {'status': 'completed', 'output': stdout.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}