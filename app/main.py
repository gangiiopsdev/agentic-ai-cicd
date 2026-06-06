from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

async def ping(host: str):
    # Secure implementation with whitelist
    allowed_hosts = {'example.com', 'localhost'}
    if host not in allowed_hosts:
        raise Exception('Host not allowed')
    args = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    if result.returncode != 0:
        raise Exception(error.decode('utf-8'))

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return await ping(host)
    except Exception as e:
        return {'error': str(e)}