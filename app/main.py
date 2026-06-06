from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate and sanitize input
    if not host.strip() or len(host) > 255:
        raise ValueError("Invalid host")

    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}