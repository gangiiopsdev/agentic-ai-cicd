from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safer implementation using subprocess.run
    args = ['ping', host]
    result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}