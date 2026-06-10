from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stderr=subprocess.PIPE, stdout=subprocess.PIPE, timeout=10)
        stdout, stderr = await output.communicate()
        if output.returncode == 0:
            return {'status': 'completed', 'output': stdout.decode('utf-8')}
        else:
            return {'status': 'error', 'error': stderr.decode('utf-8')}
    except asyncio.TimeoutError:
        return {'status': 'timeout', 'message': 'Command timed out'}