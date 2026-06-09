from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        output, error = await result.communicate()
        if result.returncode != 0:
            return {'status': 'failed', 'error': error.decode()}
        else:
            return {'status': 'completed', 'output': output.decode()}
    except asyncio.TimeoutError:
        return {'status': 'failed', 'error': 'Timeout occurred'}

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)