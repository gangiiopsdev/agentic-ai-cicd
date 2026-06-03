from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Validate or sanitize input here
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', '--', host])

@app.get("/ping")
def ping(host: str):
    await safe_ping(host)
    return {"status": "completed"}