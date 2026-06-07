from fastapi import FastAPI
import os
import asyncio

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(filter(str.isalnum, host))

async def ping(host: str):
    try:
        safe_host = sanitize_host(host)
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', safe_host, capture_output=True, text=True)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_route(host: str):
    safe_host = sanitize_host(host)
    if not all(c.isalnum() or c in ('.', '-', '_') for c in safe_host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(safe_host)