from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Safe implementation using subprocess.Popen with list for arguments
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, check=True)
    return result

def ping(host: str):
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(safe_ping(host))
    return {'status': 'completed'}