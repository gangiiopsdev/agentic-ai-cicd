from fastapi import FastAPI
import subprocess

async def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = await asyncio.subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}