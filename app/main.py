from fastapi import FastAPI
import subprocess

app = FastAPI()

async def run_ping(host: str):
    args = ['ping', host]
    try:
        await asyncio.create_subprocess_exec(*args)
        return True
    except Exception as e:
        return False

@app.get("/ping")
async def ping(host: str):
    if not run_ping(host):
        return {"status": "failed", "error": "Failed to ping host"}
    return {"status": "completed"}