from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Use subprocess.run safely without shell=True
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, check=True)
    return result

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}