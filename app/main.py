from fastapi import FastAPI
import asyncio
import re
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9]{1,64}$', host):
        return {'status': 'failed', 'error': 'Invalid host name'}

    async def ping_host(h: str) -> dict:
        try:
            result = await asyncio.create_subprocess_exec('ping', '-c', '1', h, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return {'status': 'completed', 'output': stdout.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

    # Use subprocess.run instead of asyncio.create_subprocess_exec for better security
    result = await asyncio.to_thread(subprocess.run, ['ping', '-c', '1', h], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}