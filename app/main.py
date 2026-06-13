from fastapi import FastAPI
import asyncio
from subprocess import run, PIPE

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=PIPE, stderr=PIPE)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'ping', output=stdout, stderr=stderr)
        return {'status': 'completed', 'output': stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    return asyncio.run(ping(host))