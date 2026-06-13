from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

async def safe_ping(host: str):
    if host.strip().isdigit():
        try:
            result = await asyncio.to_thread(subprocess.run, [quote('ping'), '-c', '1', quote(host)], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

@app.get('/ping')
def ping(host: str):
    return asyncio.to_thread(safe_ping, host)