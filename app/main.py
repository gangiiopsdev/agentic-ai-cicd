from fastapi import FastAPI
import subprocess

app = FastAPI()

async def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    resolved_host = await asyncio.to_thread(socket.gethostbyname, host)
    if resolved_host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}