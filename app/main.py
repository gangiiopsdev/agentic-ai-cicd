from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    if validate_host(host):
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await result.communicate()

@app.get("/ping")
def ping_host(host: str):
    return ping(host)

async def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts