from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def ping(host: str):
    # Validate the host parameter to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}

    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        output = await result.stdout.read()
        if result.returncode != 0:
            return {'status': 'failed', 'error': str(result.stderr)}
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)