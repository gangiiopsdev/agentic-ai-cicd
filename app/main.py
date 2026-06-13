from fastapi import FastAPI
import shlex
import asyncio

app = FastAPI()

async def safe_ping(host: str):
    if not host or not host.strip():
        return {'status': 'failed', 'error': 'Invalid host'}
    cmd = ['ping', shlex.quote(host)]
    try:
        result = await asyncio.create_subprocess_exec(*cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)