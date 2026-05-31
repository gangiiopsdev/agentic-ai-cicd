from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.run
    result = await asyncio.to_thread(subprocess.run, ['ping', host], capture_output=True, text=True, check=True)
    return result.stdout

def ping_route(host: str):
    try:
        output = ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}