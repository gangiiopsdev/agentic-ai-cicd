from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate and sanitize input
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode('utf-8')
    else:
        return "Unauthorized"

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)