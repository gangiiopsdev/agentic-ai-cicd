from fastapi import FastAPI
import shlex
import subprocess
import asyncio

app = FastAPI()

async def execute_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)