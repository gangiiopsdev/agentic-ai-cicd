from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    if host in ['127.0.0.1', '::1']:  # Allow only localhost for demonstration purposes
        result = await asyncio.create_subprocess_exec('ping', host)
        await result.wait()
    else:
        raise ValueError('Ping to non-localhost hosts is not allowed')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}