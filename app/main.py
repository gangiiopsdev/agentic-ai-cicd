from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.run without shell=True
    if not host:
        raise ValueError('Host parameter cannot be empty')
    try:
        await asyncio.to_thread(subprocess.run, ['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)