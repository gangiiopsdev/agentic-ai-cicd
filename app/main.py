from fastapi import FastAPI
import subprocess
import asyncio

async def ping(host: str):
    # Safer implementation using subprocess.run and input validation
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = await result.communicate()
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)