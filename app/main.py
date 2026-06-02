from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

async def safe_ping(host: str) -> str:
    if not host or len(host) > 255:
        return 'Invalid host'
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        return (await result.stdout.read()).decode()
    except Exception as e:
        return f'Ping failed with error: {e.stderr.decode()}'

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)