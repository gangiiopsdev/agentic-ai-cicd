from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

async def ping(host: str):
    try:
        # Sanitize host input more thoroughly
        safe_host = ''.join(filter(str.isalnum, host))
        result = await asyncio.create_subprocess_exec('ping', safe_host, capture_output=True, text=True)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_route(host: str):
    # Ensure host input is sanitized to prevent command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)