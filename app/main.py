from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)