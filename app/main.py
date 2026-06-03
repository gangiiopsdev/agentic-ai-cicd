from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host: str):
    # Validate input to ensure it only contains allowed characters and is a valid hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid input for ping command')
    try:
        result = await asyncio.create_subprocess_exec('ping', '-c', '4', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = await result.communicate()
        return {'status': 'completed', 'output': output[0].decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
async def ping(host: str):
    return await safe_ping(host)