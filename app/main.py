from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Ensure that host does not contain any potentially harmful characters or commands
    valid_host = ''.join(c for c in host if c.isalnum() or c in '.-')
    try:
        await asyncio.create_subprocess_exec('ping', '-c', '1', valid_host, check=True)
    except Exception as e:
        raise e

@app.get('/ping')
async def ping(host: str):
    try:
        await safe_ping(host)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}