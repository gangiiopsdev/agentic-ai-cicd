from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    result = await asyncio.to_thread(subprocess.run, ['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}