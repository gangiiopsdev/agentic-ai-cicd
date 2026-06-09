from fastapi import FastAPI
import os
import asyncio

app = FastAPI()

async def ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', host, capture_output=True, text=True)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_route(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)