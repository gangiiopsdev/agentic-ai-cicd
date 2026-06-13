from fastapi import FastAPI
import subprocess

async def safe_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode == 0:
            return {'status': 'completed'}
        else:
            return {'status': 'failed', 'error': str(error.decode())}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent command injection
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return await safe_ping(host)

import re
async def validate_host(host: str) -> bool:
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None