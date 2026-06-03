from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

async def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        output = await asyncio.to_thread(subprocess.check_output, ['ping', '-c', '4', safe_host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)