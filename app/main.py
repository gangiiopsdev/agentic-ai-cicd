from fastapi import FastAPI
import subprocess

app = FastAPI()

async def run_ping(host: str):
    args = ['ping', host]
    result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)
    return result.stdout

def ping(host: str):
    output = run_ping(host)
    return {"status": "completed", "output": output}