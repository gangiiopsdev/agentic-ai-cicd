from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    args = ['ping', host]
    process = await asyncio.create_subprocess_exec(*args)
    await process.wait()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    await safe_ping(host)
    return {"status": "completed"}

async def is_safe_host(host):
    # Add your logic to validate the host
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts