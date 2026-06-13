from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            raise subprocess.CalledProcessError(returncode=output.returncode, cmd='ping', output=stderr.decode())
        return {'status': 'completed', 'output': stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}