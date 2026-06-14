from fastapi import FastAPI
import asyncio
from sanic.response import json

app = FastAPI()

async def safe_ping(host):
    try:
        # Sanitize input
        host = subprocess.list2cmdline([host])
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
async def ping(host: str):
    # Safer implementation
    return await safe_ping(host)